# +----------------------------------------------------------------------------+
# | B3DESK                                                                  |
# +----------------------------------------------------------------------------+
#
#   This program is free software: you can redistribute it and/or modify it
# under the terms of the European Union Public License 1.2 version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
import hashlib
import json
from datetime import date
from datetime import datetime
from datetime import timezone

from flask import current_app

from b3desk.models.groups import Group
from b3desk.nextcloud import update_user_nc_credentials
from b3desk.utils import secret_key

from . import db


def get_or_create_user(user_info):
    """Get existing user by email or create a new user from user_info dictionary.

    Updates user information if any fields have changed and saves to database.
    """
    mapping = current_app.config["OIDC_CLAIMS_MAPPING"]
    given_name = user_info.get(mapping.get("given_name", "given_name"), "")
    family_name = user_info.get(mapping.get("family_name", "family_name"), "")
    preferred_username = user_info.get(
        mapping.get("preferred_username", "preferred_username")
    )
    email = user_info[mapping.get("email", "email")].lower()

    meta_data = json.dumps(
        {
            "academic_domain": user_info.get(mapping.get("FrEduAca", "FrEduAca"), ""),
        }
    )

    user = User.get_user_by_email(email)

    if user is None:
        user = User(
            email=email,
            given_name=given_name,
            family_name=family_name,
            preferred_username=preferred_username,
            last_connection_utc_datetime=datetime.now(timezone.utc),
            meta_data=meta_data,
        )
        update_user_nc_credentials(user)
        db.session.add(user)
        db.session.commit()

    else:
        user_changes = update_user_nc_credentials(user) or {}

        if user.given_name != given_name:
            user.given_name = given_name
            user_changes["given_name"] = given_name

        if user.family_name != family_name:
            user.family_name = family_name
            user_changes["family_name"] = family_name

        if user.preferred_username != preferred_username:
            user.preferred_username = preferred_username
            user_changes["preferred_username"] = preferred_username

        if (
            not user.last_connection_utc_datetime
            or user.last_connection_utc_datetime.date() < date.today()
        ):
            user.last_connection_utc_datetime = datetime.now(timezone.utc)
            user_changes["last_connection_utc_datetime"] = datetime.now(timezone.utc)

        if user.meta_data and user.meta_data != meta_data:
            user.meta_data = meta_data
            user_changes["meta_data"] = meta_data

        if user_changes:
            db.session.add(user)
            db.session.commit()
            current_app.logger.info("%s has changed %s", user.email, user_changes)

    user.automatic_group_affiliation()

    return user


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Unicode(255), unique=True)
    given_name = db.Column(db.Unicode(50))
    family_name = db.Column(db.Unicode(50))
    preferred_username = db.Column(db.Unicode(255), nullable=True)
    nc_locator = db.Column(db.Unicode(255))
    nc_login = db.Column(db.Unicode(255))
    nc_token = db.Column(db.Unicode(255))
    nc_last_auto_enroll = db.Column(db.DateTime)
    last_connection_utc_datetime = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)
    meta_data = db.Column(db.JSON)

    meetings = db.relationship("Meeting", back_populates="owner")
    favorites = db.relationship(
        "Meeting", secondary="favorite", back_populates="favorite_of"
    )
    groups = db.relationship(
        "Group", secondary="group_member", back_populates="members"
    )
    excluded_groups = db.relationship(
        "Group", secondary="excludelist", back_populates="excluded_users"
    )

    @property
    def fullname(self):
        """Return user's full name combining given name and family name."""
        return f"{self.given_name} {self.family_name}"

    @property
    def hash(self):
        """Generate SHA1 hash from user's email and application secret key."""
        s = f"{self.email}|{secret_key()}"
        return hashlib.sha1(s.encode("utf-8")).hexdigest()

    @property
    def can_create_meetings(self):
        """Check if user has not reached the maximum number of meetings allowed."""
        return len(self.meetings) < current_app.config["MAX_MEETINGS_PER_USER"]

    @property
    def has_nc_credentials(self):
        """Check if user has valid Nextcloud credentials (login, token, and locator)."""
        return bool(self.nc_login and self.nc_token and self.nc_locator)

    @property
    def mail_domain(self):
        """Extract and return the domain from meta_data or part of the user's email address."""
        if self.meta_data:
            user_meta_data = json.loads(self.meta_data)
            return user_meta_data["academic_domain"]
        return self.email.split("@")[1] if self.email and "@" in self.email else None

    @property
    def get_all_delegated_meetings(self):
        from b3desk.models.meetings import AccessLevel
        from b3desk.models.meetings import Meeting
        from b3desk.models.meetings import MeetingAccess

        return (
            Meeting.query.join(MeetingAccess)
            .filter(
                MeetingAccess.user_id == self.id,
                MeetingAccess.level == AccessLevel.DELEGATE,
            )
            .all()
        )

    @classmethod
    def get_user_by_email(cls, email):
        return db.session.query(User).filter(User.email == email).first()

    @property
    def can_use_file_sharing(self):
        if not self.groups:
            return current_app.config["FILE_SHARING"]
        if any(group.enable_file_sharing for group in self.groups):
            return True
        if all(group.enable_file_sharing is False for group in self.groups):
            return False
        return current_app.config["FILE_SHARING"]

    @property
    def can_use_sip(self):
        if not self.groups:
            return current_app.config["ENABLE_SIP"]
        if any(group.enable_sip for group in self.groups):
            return True
        if all(group.enable_sip is False for group in self.groups):
            return False
        return current_app.config["ENABLE_SIP"]

    @property
    def can_use_ai_summary(self):
        if not self.groups:
            return current_app.config["ENABLE_AI_SUMMARY"]
        if any(group.enable_ai_summary for group in self.groups):
            return True
        if all(group.enable_ai_summary is False for group in self.groups):
            return False
        return current_app.config["ENABLE_AI_SUMMARY"]

    def automatic_group_affiliation(self):
        groups = db.session.execute(db.select(Group)).scalars().all()
        added_groups = []
        removed_groups = []
        for group in groups:
            if (
                self not in group.excluded_users
                and self.mail_domain in group.academic_domains
            ):
                group.members.append(self)
                added_groups.append((group.id, group.name))
            if self in group.excluded_users and self in group.members:
                group.members.remove(self)
                removed_groups.append((group.id, group.name))

        for group in added_groups:
            current_app.logger.info(
                "%s added in group %s %s", self.fullname, group[0], group[1]
            )
        for group in removed_groups:
            current_app.logger.info(
                "%s removed from group %s %s", self.fullname, group[0], group[1]
            )

        if added_groups or removed_groups:
            db.session.commit()
