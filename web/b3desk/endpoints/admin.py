from flask import Blueprint
from flask import current_app
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_babel import lazy_gettext as _
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

from b3desk.forms import AcademicDomainForm
from b3desk.forms import GroupForm
from b3desk.forms import GroupSearchForm
from b3desk.forms import MeetingSearchForm
from b3desk.forms import UserExclusionForm
from b3desk.forms import UserSearchForm
from b3desk.join import get_signin_url
from b3desk.models import db
from b3desk.models.groups import Group
from b3desk.models.meetings import Meeting
from b3desk.models.roles import Role
from b3desk.models.users import User

from ..session import admin_needed

bp = Blueprint("admin", __name__)


PER_PAGE = 50


def get_groups_paginate(per_page, data):
    query = db.select(Group).order_by(Group.created_at)
    if data:
        query = query.where(
            or_(
                Group.id == int(data) if data.isdigit() else None,
                Group.name.ilike(f"%{data}%"),
            )
        )
    return db.paginate(query, per_page=per_page)


def get_meetings_paginate(per_page, data):
    query = db.select(Meeting).order_by(Meeting.created_at)
    if data:
        query = query.where(
            or_(
                Meeting.id == int(data) if data.isdigit() else None,
                Meeting.name.ilike(f"%{data}%"),
                Meeting.visio_code == data,
            )
        )
    return db.paginate(query, per_page=per_page)


def get_group_members_paginate(group, per_page, data=None):
    members = group.get_all_members
    if data:
        members = members.where(
            or_(
                User.id == int(data) if data.isdigit() else None,
                User.given_name.ilike(f"%{data}%"),
                User.family_name.ilike(f"%{data}%"),
                User.email.ilike(f"%{data}%"),
            )
        )
    return db.paginate(members, per_page=per_page)


def get_users_paginate(per_page, data=None):
    query = db.select(User).order_by(User.created_at)
    if data:
        query = query.where(
            or_(
                User.id == int(data) if data.isdigit() else None,
                User.given_name.ilike(f"%{data}%"),
                User.family_name.ilike(f"%{data}%"),
                User.email.ilike(f"%{data}%"),
            )
        )
    return db.paginate(query, per_page=per_page)


def get_all_users_not_in_group(group, data=None):
    query = (
        db.select(User).where(~User.groups.contains(group)).order_by(User.created_at)
    )
    if data:
        query = query.where(
            or_(
                User.id == int(data) if data.isdigit() else None,
                User.given_name.ilike(f"%{data}%"),
                User.family_name.ilike(f"%{data}%"),
                User.email.ilike(f"%{data}%"),
            )
        )
    return db.session.execute(query).scalars().all()


def get_excluded_users_paginate(group, per_page):
    members = group.get_all_exclude_users
    return db.paginate(members, per_page=per_page)


@bp.route("/admin/home")
@admin_needed
def home():
    """Display the menu of admin page."""
    return render_template(
        "admin/home.html",
    )


@bp.route("/admin/users")
@admin_needed
def manage_users():
    """Display user list to manage users."""
    form = UserSearchForm(request.args, meta={"csrf": False})
    data = form.search.data.lower() if form.search.data else None
    users_page = get_users_paginate(per_page=PER_PAGE, data=data)
    return render_template(
        "admin/users.html",
        admin_mode=True,
        users_page=users_page,
        form=form,
        data=data,
        group=None,
        add_members=False,
    )


@bp.route("/admin/user/<user:user>")
@admin_needed
def user_infos(user: User):
    """Display user infos."""
    return render_template(
        "admin/user_infos.html",
        admin_mode=True,
        user=user,
    )


@bp.route("/admin/meetings")
@admin_needed
def manage_meetings():
    """Display meeting list to manage meetings."""
    form = MeetingSearchForm(request.args, meta={"csrf": False})
    data = form.search.data.lower() if form.search.data else None
    meetings_page = get_meetings_paginate(per_page=PER_PAGE, data=data)
    return render_template(
        "admin/meetings.html",
        admin_mode=True,
        meetings_page=meetings_page,
        form=form,
        data=data,
    )


@bp.route("/admin/meeting/<meeting:meeting>")
@admin_needed
def meeting_infos(meeting: Meeting):
    """Display meeting infos of admin page."""
    meeting.moderator_url = get_signin_url(meeting, Role.moderator)
    meeting.attendee_url = get_signin_url(meeting, Role.attendee)
    meeting.authenticated_url = get_signin_url(meeting, Role.authenticated)
    return render_template(
        "admin/meeting_infos.html",
        admin_mode=True,
        meeting=meeting,
    )


@bp.route("/admin/create-group", methods=["GET", "POST"])
@admin_needed
def create_group():
    """Display group creation of admin page."""
    form = GroupForm(request.form)
    if not request.form or not form.validate():
        return render_template(
            "admin/group_form.html",
            group=None,
            form=form,
            data=None,
        )
    group = Group()
    form.populate_obj(group)
    db.session.add(group)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        form.name.errors.append(_("Ce nom est déjà utilisé."))
        return render_template(
            "admin/group_form.html",
            group=None,
            form=form,
            data=None,
        )

    current_app.logger.info(
        "Group %s %s was created by %s",
        group.name,
        group.id,
        g.user.email,
    )
    flash(
        _("{group_name} a bien été créé(e)").format(group_name=group.name),
        "success",
    )
    return redirect(url_for("admin.group_infos", group=group))


@bp.route("/admin/group/<group:group>")
@admin_needed
def group_infos(group: Group):
    """Display group infos of admin page."""
    return render_template(
        "admin/group_infos.html",
        group=group,
    )


@bp.route("/admin/groups", methods=["GET", "POST"])
@admin_needed
def manage_groups():
    """Display group list to manage groups of admin page."""
    form = GroupSearchForm(request.form)
    if not request.form or not form.validate():
        groups_page = get_groups_paginate(per_page=PER_PAGE, data=None)
        return render_template(
            "admin/groups.html",
            groups_page=groups_page,
            form=form,
            data=None,
        )
    data = form.search.data.lower()
    groups_page = get_groups_paginate(per_page=PER_PAGE, data=data)
    return render_template(
        "admin/groups.html",
        groups_page=groups_page,
        form=form,
        data=data,
    )


@bp.route("/admin/edit-group/<group:group>", methods=["GET", "POST"])
@admin_needed
def edit_group(group: Group):
    """Display group settings for group edition of admin page."""
    form = GroupForm(request.form if request.method == "POST" else None, obj=group)
    domain_form = AcademicDomainForm(request.form)
    if request.method == "GET":
        return render_template(
            "admin/group_form.html",
            form=form,
            domain_form=domain_form,
            group=group,
        )

    if not form.validate():
        flash(_("Le formulaire contient des erreurs"), "error")
        return render_template(
            "admin/group_form.html",
            form=form,
            domain_form=domain_form,
            group=group,
        )

    del form.id

    updated_data = {
        key: form.data[key]
        for key in form.data
        if hasattr(group, key) and getattr(group, key) != form.data[key]
    }
    form.populate_obj(group)
    db.session.add(group)
    db.session.commit()
    current_app.logger.info(
        "Group %s %s was updated by %s. Updated fields : %s",
        group.name,
        group.id,
        g.user.email,
        updated_data,
    )
    flash(
        _("%(group_name)s modifications prises en compte", group_name=group.name),
        "success",
    )

    return redirect(url_for("admin.group_infos", group=group))


@bp.route("/admin/manage-group-members/<group:group>", methods=["GET", "POST"])
@admin_needed
def manage_group_members(group: Group):
    """Display group members list and member addition of admin page."""
    form = UserSearchForm(request.args, meta={"csrf": False})
    data = form.search.data.lower() if form.search.data else None
    members_page = get_group_members_paginate(group, per_page=PER_PAGE, data=data)
    return render_template(
        "admin/group_members.html",
        group=group,
        form=form,
        members_page=members_page,
        data=data,
        add_members=False,
    )


@bp.route("/admin/manage-group-members/<group:group>/<user:member>")
@admin_needed
def remove_member(group: Group, member: User):
    """Display group members list and member removing admin page."""
    form = UserSearchForm(request.args, meta={"csrf": False})
    data = form.search.data.lower() if form.search.data else None
    if member not in group.members:
        flash(_("L'utilisateur ne fait pas partie du groupe"), "error")
    else:
        group.members.remove(member)
        db.session.commit()
        flash(_("L'utilisateur a été retiré du groupe"), "success")
        current_app.logger.info(
            "%s member removed from group %s %s",
            member.email,
            group.id,
            group.name,
        )
    members_page = get_group_members_paginate(group, per_page=PER_PAGE, data=data)
    return render_template(
        "admin/group_members.html",
        group=group,
        form=form,
        members_page=members_page,
        data=data,
        add_members=False,
    )


@bp.route("/admin/delete-group/<group:group>")
@admin_needed
def delete_group(group: Group):
    """Display group deletion of admin page."""
    return render_template(
        "admin/delete_group.html",
        group=group,
    )


@bp.route("/admin/confirm-delete-group/<group:group>")
@admin_needed
def confirm_delete_group(group: Group):
    """Display group deletion of admin page."""
    db.session.delete(group)
    db.session.commit()
    flash(_("Le groupe a été supprimé"), "success")
    current_app.logger.info("Groupe %s %s deleted", group.id, group.name)
    return redirect(url_for("admin.manage_groups"))


def add_users_in_group(selected_users, group, ids=False):
    added_users = []
    for user in selected_users:
        user = db.session.get(User, int(user)) if ids else user
        if user and user not in group.members:
            group.members.append(user)
            added_users.append(user)
    db.session.commit()
    for user in added_users:
        current_app.logger.info(
            "%s became member of group %s %s", user.email, group.id, group.name
        )
    flash(
        _(f"{len(added_users)} membre(s) ajouté(s) au groupe"),
        "success",
    )


@bp.route("/admin/add-group-members/<group:group>", methods=["GET", "POST"])
@admin_needed
def add_group_members(group: Group):
    """Display non member users list to add members."""
    form = UserSearchForm(request.args, meta={"csrf": False})
    select_all = (
        bool(request.values.get("select_all"))
        if request.values.get("select_all")
        else False
    )

    if request.method == "GET":
        data = form.search.data.lower() if form.search.data else None
    else:
        data = (
            request.form.get("search").lower() if request.form.get("search") else None
        )

    selected_users = get_all_users_not_in_group(group, data)
    users_page = get_users_paginate(per_page=PER_PAGE, data=data)

    if request.method == "POST":
        user_ids = request.form.getlist("user_ids")
        if select_all and selected_users:
            add_users_in_group(selected_users, group)
        elif user_ids:
            add_users_in_group(user_ids, group, ids=True)
        else:
            flash(_("Vous n'avez pas sélectionné d'utilisateur"), "message")
        return redirect(
            url_for(
                "admin.add_group_members",
                group=group,
                search=data,
                select_all=1 if select_all else None,
            )
        )

    return render_template(
        "admin/add_group_members.html",
        group=group,
        search=data,
        form=form,
        users_page=users_page,
        data=data,
        add_members=True,
        selected_users=selected_users,
        select_all=select_all,
    )


@bp.route("/admin/academic-domain/<group:group>", methods=["GET", "POST"])
@admin_needed
def manage_academic_domain(group: Group):
    """Display and manage a group's academic domains."""
    form = AcademicDomainForm(request.form)

    if request.method == "GET":
        return render_template(
            "admin/group_academic_domain.html",
            form=form,
            group=group,
        )

    if not form.validate():
        flash(_("Le formulaire contient des erreurs"), "error")
        return render_template(
            "admin/group_academic_domain.html",
            form=form,
            group=group,
        )

    new_domain = form.data["academic_domain"]
    if new_domain not in group.academic_domains:
        group.academic_domains.append(new_domain)
        db.session.commit()
        current_app.logger.info(
            "%s a été ajouté à la liste du groupe %s %s",
            new_domain,
            group.id,
            group.name,
        )
    else:
        flash(
            _("{new_domain} est déjà dans la liste du groupe {group_name}").format(
                new_domain=new_domain, group_name=group.name
            ),
            "error",
        )

    return render_template(
        "admin/group_academic_domain.html",
        form=form,
        group=group,
    )


@bp.route("/admin/remove-academic-domain/<group:group>")
@admin_needed
def remove_academic_domain(group: Group):
    """Remove academic domain from group."""
    form = AcademicDomainForm(request.form)
    domain = request.args["domain"]
    if domain in group.academic_domains:
        group.academic_domains.remove(domain)
        db.session.commit()
        current_app.logger.info(
            "%s a été retiré le la liste du groupe %s %s", domain, group.id, group.name
        )

    return render_template(
        "admin/group_academic_domain.html",
        form=form,
        group=group,
    )


@bp.route("/admin/excluded-users/<group:group>", methods=["GET", "POST"])
@admin_needed
def manage_excluded_users(group: Group):
    form = UserExclusionForm(request.form)

    if request.method == "GET":
        excluded_users_page = get_excluded_users_paginate(group, per_page=PER_PAGE)
        return render_template(
            "admin/group_excluded_users.html",
            form=form,
            group=group,
            excluded_users_page=excluded_users_page,
            add_members=False,
            remove_excluded_users=True,
        )

    if not form.validate():
        excluded_users_page = get_excluded_users_paginate(group, per_page=PER_PAGE)
        flash(_("Le formulaire contient des erreurs"), "error")
        return render_template(
            "admin/group_excluded_users.html",
            form=form,
            group=group,
            excluded_users_page=excluded_users_page,
            add_members=False,
            remove_excluded_users=True,
        )

    email = form.data["search"]
    user = User.get_user_by_email(email)
    current_app.logger.warning(email)
    current_app.logger.warning(user)
    if user not in group.excluded_users:
        group.excluded_users.append(user)
        db.session.commit()
    else:
        flash(_("L'utilisateur est déjà pas dans la liste"), "error")
    excluded_users_page = get_excluded_users_paginate(group, per_page=PER_PAGE)
    return render_template(
        "admin/group_excluded_users.html",
        form=form,
        group=group,
        excluded_users_page=excluded_users_page,
        add_members=False,
        remove_excluded_users=True,
    )


@bp.route("/admin/excluded-users/<group:group>/<user:user>")
@admin_needed
def remove_excluded_users(group: Group, user: User):
    form = UserExclusionForm(request.form)

    if user not in group.excluded_users:
        flash(_("L'utilisateur n'est pas dans la liste"), "error")
    else:
        group.excluded_users.remove(user)
        db.session.commit()
        current_app.logger.info(
            "%s a été retiré le la liste du groupe %s %s",
            user.fullname,
            group.id,
            group.name,
        )

    excluded_users_page = get_excluded_users_paginate(group, per_page=PER_PAGE)
    return render_template(
        "admin/group_excluded_users.html",
        form=form,
        group=group,
        excluded_users_page=excluded_users_page,
        add_members=False,
        remove_excluded_users=True,
    )
