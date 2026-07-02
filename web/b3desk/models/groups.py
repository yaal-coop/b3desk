from datetime import datetime

from sqlalchemy.ext.mutable import MutableList

from . import db

group_member_table = db.Table(
    "group_member",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("group.id"), primary_key=True),
)

excludelist_table = db.Table(
    "excludelist",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("group_id", db.Integer, db.ForeignKey("group.id"), primary_key=True),
)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    name = db.Column(db.Unicode(150), unique=True)
    enable_sip = db.Column(db.Boolean, default=None)
    enable_file_sharing = db.Column(db.Boolean, default=None)
    enable_ai_summary = db.Column(db.Boolean, default=None)
    academic_domains = db.Column(MutableList.as_mutable(db.JSON), default=list)

    members = db.relationship(
        "User", secondary=group_member_table, back_populates="groups"
    )
    excluded_users = db.relationship(
        "User", secondary=excludelist_table, back_populates="excluded_groups"
    )

    @property
    def get_all_members(self):
        from b3desk.models.users import User

        return (
            db.select(User)
            .join(group_member_table, User.id == group_member_table.c.user_id)
            .where(group_member_table.c.group_id == self.id)
            .order_by(User.family_name, User.given_name)
        )

    @property
    def get_all_exclude_users(self):
        from b3desk.models.users import User

        return (
            db.select(User)
            .join(excludelist_table, User.id == excludelist_table.c.user_id)
            .where(excludelist_table.c.group_id == self.id)
            .order_by(User.family_name, User.given_name)
        )
