# +----------------------------------------------------------------------------+
# | BBB-VISIO                                                                  |
# +----------------------------------------------------------------------------+
#
#   This program is free software: you can redistribute it and/or modify it
# under the terms of the European Union Public License 1.2 version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.
import hashlib
import secrets
import uuid
from datetime import datetime
from pathlib import Path

import requests
from b3desk.forms import EndMeetingForm
from b3desk.forms import JoinMailMeetingForm
from b3desk.forms import JoinMeetingForm
from b3desk.forms import MeetingFilesForm
from b3desk.forms import MeetingForm
from b3desk.forms import MeetingWithRecordForm
from b3desk.forms import RecordingForm
from b3desk.forms import ShowMeetingForm
from b3desk.models import db
from b3desk.models.meetings import get_mail_meeting
from b3desk.models.meetings import get_meeting_from_meeting_id_and_user_id
from b3desk.models.meetings import get_quick_meeting_from_user_and_random_string
from b3desk.models.meetings import Meeting
from b3desk.models.meetings import MeetingFiles
from b3desk.models.meetings import MeetingFilesExternal
from b3desk.models.users import get_or_create_user
from b3desk.models.users import User
from flask import abort
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file
from flask import send_from_directory
from flask import url_for
from flask_babel import lazy_gettext as _
from webdav3.client import Client as webdavClient
from webdav3.exceptions import WebDavException

from .. import auth
from ..session import get_authenticated_attendee_fullname
from ..session import get_current_user
from ..session import has_user_session
from ..utils import is_accepted_email
from ..utils import is_valid_email
from ..utils import send_quick_meeting_mail


bp = Blueprint("meetings", __name__)


def meeting_mailto_params(meeting, role):
    if role == "moderator":
        return render_template(
            "meeting/mailto/mail_href.txt", meeting=meeting, role="moderator"
        ).replace("\n", "%0D%0A")
    elif role == "attendee":
        return render_template(
            "meeting/mailto/mail_href.txt", meeting=meeting, role="attendee"
        ).replace("\n", "%0D%0A")


@bp.route("/api/meetings")
@auth.token_auth(provider_name="default")
def api_meetings():
    # TODO: probably unused
    if not auth.current_token_identity:
        return redirect(url_for("public.index"))

    info = {
        "given_name": auth.current_token_identity["given_name"],
        "family_name": auth.current_token_identity["family_name"],
        "email": auth.current_token_identity["email"],
    }
    user = get_or_create_user(info)
    return {
        "meetings": [
            {
                "name": m.name,
                "moderator_url": m.get_signin_url("moderator"),
                "attendee_url": m.get_signin_url("attendee"),
            }
            for m in user.meetings
        ]
    }


@bp.route("/meeting/mail", methods=["POST"])
def quick_mail_meeting():
    #### Almost the same as quick meeting but we do not redirect to join
    email = request.form.get("mail")
    if not is_valid_email(email):
        flash(
            _(
                "Courriel invalide. Avez vous bien tapé votre email ? Vous pouvez réessayer."
            ),
            "error_login",
        )
        return redirect(url_for("public.index"))
    if not is_accepted_email(email):
        flash(
            _(
                "Ce courriel ne correspond pas à un service de l'État. Si vous appartenez à un service de l'État mais votre courriel n'est pas reconnu par Webinaire, contactez-nous pour que nous le rajoutions !"
            ),
            "error_login",
        )
        return redirect(url_for("public.index"))
    user = User(
        id=email
    )  # this user can probably be removed if we created adock function
    meeting = get_quick_meeting_from_user_and_random_string(user)
    send_quick_meeting_mail(meeting, email)
    flash(_("Vous avez reçu un courriel pour vous connecter"), "success_login")
    return redirect(url_for("public.index"))


@bp.route("/meeting/quick")
@auth.oidc_auth("default")
def quick_meeting():
    user = get_current_user()
    meeting = get_quick_meeting_from_user_and_random_string(user)
    return redirect(meeting.get_join_url("moderator", user.fullname, create=True))


@bp.route("/meeting/show/<meeting:meeting>")
@auth.oidc_auth("default")
def show_meeting(meeting):
    # TODO: appears unused

    form = ShowMeetingForm(data={"meeting_id": meeting.id})
    if not form.validate():
        flash(
            _("Vous ne pouvez pas voir cet élément (identifiant incorrect)"),
            "warning",
        )
        return redirect(url_for("public.welcome"))
    user = get_current_user()
    if meeting.user_id == user.id:
        return render_template(
            "meeting/show.html",
            meeting_mailto_params=meeting_mailto_params,
            meeting=meeting,
        )
    flash(_("Vous ne pouvez pas consulter cet élément"), "warning")
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/recordings/<meeting:meeting>")
@auth.oidc_auth("default")
def show_meeting_recording(meeting):
    user = get_current_user()
    if meeting.user_id == user.id:
        form = RecordingForm()
        return render_template(
            "meeting/recordings.html",
            meeting_mailto_params=meeting_mailto_params,
            meeting=meeting,
            form=form,
        )
    flash(_("Vous ne pouvez pas consulter cet élément"), "warning")
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/<meeting:meeting>/recordings/<recording_id>", methods=["POST"])
@auth.oidc_auth("default")
def update_recording_name(meeting, recording_id):
    user = get_current_user()
    if meeting.user_id == user.id:
        form = RecordingForm(request.form)
        form.validate() or abort(403)
        result = meeting.update_recording_name(recording_id, form.data["name"])
        return_code = result.get("returncode")
        if return_code == "SUCCESS":
            flash("Enregistrement renommé", "success")
        else:
            message = result.get("message", "")
            flash(
                "Nous n'avons pas pu modifier cet enregistrement : {code}, {message}".format(
                    code=return_code, message=message
                ),
                "error",
            )
    else:
        flash("Vous ne pouvez pas modifier cet enregistrement", "error")
    return redirect(url_for("meetings.show_meeting_recording", meeting=meeting))


@bp.route("/meeting/new")
@auth.oidc_auth("default")
def new_meeting():
    user = get_current_user()
    if not user.can_create_meetings:
        return redirect(url_for("public.welcome"))

    form = MeetingWithRecordForm() if current_app.config["RECORDING"] else MeetingForm()

    return render_template(
        "meeting/wizard.html",
        meeting=None,
        form=form,
        recording=current_app.config["RECORDING"],
    )


@bp.route("/meeting/edit/<meeting:meeting>")
@auth.oidc_auth("default")
def edit_meeting(meeting):
    user = get_current_user()

    form = (
        MeetingWithRecordForm(obj=meeting)
        if current_app.config["RECORDING"]
        else MeetingForm(obj=meeting)
    )
    if meeting and meeting.user_id == user.id:
        return render_template(
            "meeting/wizard.html",
            meeting=meeting,
            form=form,
            recording=current_app.config["RECORDING"],
        )
    flash("Vous ne pouvez pas modifier cet élément", "warning")
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/files/<meeting:meeting>")
@auth.oidc_auth("default")
def edit_meeting_files(meeting):
    user = get_current_user()

    form = MeetingFilesForm()

    if current_app.config["FILE_SHARING"]:
        # we test webdav connection here, with a simple 'list' command
        if user.nc_login and user.nc_token and user.nc_locator:
            options = {
                "webdav_root": f"/remote.php/dav/files/{user.nc_login}/",
                "webdav_hostname": user.nc_locator,
                "webdav_verbose": True,
                "webdav_token": user.nc_token,
            }
            try:
                client = webdavClient(options)
                client.list()
            except WebDavException as exception:
                current_app.logger.warning(
                    "WebDAV error, user data disabled: %s", exception
                )
                user.disable_nextcloud()

        if user is not None and meeting.user_id == user.id:
            return render_template(
                "meeting/filesform.html",
                meeting=meeting,
                form=form,
            )
    flash(_("Vous ne pouvez pas modifier cet élément"), "warning")
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/files/<meeting:meeting>/")
@bp.route("/meeting/files/<meeting:meeting>/<int:file_id>")
@auth.oidc_auth("default")
def download_meeting_files(meeting, file_id=None):
    user = get_current_user()

    TMP_DOWNLOAD_DIR = current_app.config["TMP_DOWNLOAD_DIR"]
    Path(TMP_DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)
    tmpName = f'{current_app.config["TMP_DOWNLOAD_DIR"]}{secrets.token_urlsafe(32)}'
    fileToSend = None
    if user is not None and meeting.user_id == user.id:
        for curFile in meeting.files:
            if curFile.id == file_id:
                fileToSend = curFile
                break
        if not fileToSend:
            return jsonify(status=404, msg="file not found")
        if curFile.url:
            response = requests.get(curFile.url)
            open(tmpName, "wb").write(response.content)
            return send_file(tmpName, as_attachment=True, download_name=curFile.title)
        else:
            # get file from nextcloud WEBDAV and send it
            try:
                davUser = {
                    "nc_locator": user.nc_locator,
                    "nc_login": user.nc_login,
                    "nc_token": user.nc_token,
                }
                options = {
                    "webdav_root": f"/remote.php/dav/files/{davUser['nc_login']}/",
                    "webdav_hostname": davUser["nc_locator"],
                    "webdav_verbose": True,
                    "webdav_token": davUser["nc_token"],
                }
                client = webdavClient(options)
                kwargs = {
                    "remote_path": curFile.nc_path,
                    "local_path": f"{tmpName}",
                }
                client.download_sync(**kwargs)
                return send_file(
                    tmpName, as_attachment=True, download_name=curFile.title
                )
            except WebDavException as exception:
                user.disable_nextcloud()
                current_app.logger.warning(
                    "webdav call encountered following exception : %s", exception
                )
                flash("Le fichier ne semble pas accessible", "error")
                return redirect(url_for("public.welcome"))
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/save", methods=["POST"])
@auth.oidc_auth("default")
def save_meeting():
    user = get_current_user()
    form = (
        MeetingWithRecordForm(request.form)
        if current_app.config["RECORDING"]
        else MeetingForm(request.form)
    )

    is_new_meeting = not form.data["id"]
    if not user.can_create_meetings and is_new_meeting:
        return redirect(url_for("public.welcome"))

    if not form.validate():
        flash("Le formulaire contient des erreurs", "error")
        return render_template(
            "meeting/wizard.html",
            meeting=None if is_new_meeting else db.session.get(Meeting, form.id.data),
            form=form,
            recording=current_app.config["RECORDING"],
        )

    if is_new_meeting:
        meeting = Meeting()
        meeting.user = user
    else:
        meeting_id = form.data["id"]
        meeting = db.session.get(Meeting, meeting_id)
        del form.id
        del form.name

    meeting.record = bool(
        form.data.get("allowStartStopRecording") or form.data.get("autoStartRecording")
    )
    form.populate_obj(meeting)
    meeting.save()
    flash(
        _("%(meeting_name)s modifications prises en compte", meeting_name=meeting.name),
        "success",
    )

    if meeting.is_running():
        return render_template(
            "meeting/end.html",
            meeting=meeting,
            form=EndMeetingForm(data={"meeting_id": meeting_id}),
        )
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/end", methods=["POST"])
@auth.oidc_auth("default")
def end_meeting():
    user = get_current_user()
    form = EndMeetingForm(request.form)

    meeting_id = form.data["meeting_id"]
    meeting = db.session.get(Meeting, meeting_id) or abort(404)

    if user == meeting.user:
        meeting.end_bbb()
        flash(
            f"{current_app.config['WORDING_MEETING'].capitalize()} « {meeting.name} » terminé(e)",
            "success",
        )
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/create/<meeting:meeting>")
@auth.oidc_auth("default")
def create_meeting(meeting):
    user = get_current_user()
    if meeting.user_id == user.id:
        meeting.create_bbb()
        meeting.save()
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/<meeting:meeting>/externalUpload")
@auth.oidc_auth("default")
def externalUpload(meeting):
    user = get_current_user()
    if meeting.is_running() and user is not None and meeting.user_id == user.id:
        return render_template("meeting/externalUpload.html", meeting=meeting)
    return redirect(url_for("public.welcome"))


@bp.route("/ncdownload/<isexternal>/<mfid>/<mftoken>")
# @auth.token_auth(provider_name="default") - must be accessible by BBB server, so no auth
def ncdownload(isexternal, mfid, mftoken):
    secret_key = current_app.config["SECRET_KEY"]
    # select good file from token
    # get file through NC credentials - HOW POSSIBLE ?
    # return file as response to BBB server
    # isexternal tells if the file has been chosen earlier from the visio-agent interface (0) or if it has been uploaded from BBB itself (1)
    if str(isexternal) == "0":
        isexternal = "0"
        meeting_file = MeetingFiles.query.filter_by(id=mfid).one_or_none()
    else:
        isexternal = "1"
        meeting_file = MeetingFilesExternal.query.filter_by(id=mfid).one_or_none()

    if not meeting_file:
        return make_response("Bad token provided, no file matching", 404)

    # the hash token consist of the sha1 of "secret key - 0/1 (internal/external) - id in the DB - secret key"
    if (
        mftoken
        != hashlib.sha1(
            f"{secret_key}-{isexternal}-{mfid}-{secret_key}".encode()
        ).hexdigest()
    ):
        return make_response("Bad token provided, no file matching", 404)

    # download the file using webdavClient from the Nextcloud to a temporary folder (that will need cleaning)
    options = {
        "webdav_root": f"/remote.php/dav/files/{meeting_file.meeting.user.nc_login}/",
        "webdav_hostname": meeting_file.meeting.user.nc_locator,
        "webdav_verbose": True,
        "webdav_token": meeting_file.meeting.user.nc_token,
    }
    try:
        client = webdavClient(options)
        TMP_DOWNLOAD_DIR = current_app.config["TMP_DOWNLOAD_DIR"]
        Path(TMP_DOWNLOAD_DIR).mkdir(parents=True, exist_ok=True)
        uniqfile = str(uuid.uuid4())
        tmpName = f"{TMP_DOWNLOAD_DIR}{uniqfile}"
        kwargs = {
            "remote_path": meeting_file.nc_path,
            "local_path": tmpName,
        }
        client.download_sync(**kwargs)
    except WebDavException:
        meeting_file.meeting.user.disable_nextcloud()
        return jsonify(status=500, msg="La connexion avec Nextcloud semble rompue")
    # send the downloaded file to the BBB:
    return send_from_directory(TMP_DOWNLOAD_DIR, uniqfile)


@bp.route(
    "/meeting/signinmail/<meeting_fake_id>/expiration/<expiration>/hash/<h>",
)
def signin_mail_meeting(meeting_fake_id, expiration, h):
    meeting = get_mail_meeting(meeting_fake_id)
    wordings = current_app.config["WORDINGS"]

    if meeting is None:
        flash(
            _(
                "Aucune %(meeting_label)s ne correspond à ces paramètres",
                meeting_label=wordings["meeting_label"],
            ),
            "success",
        )
        return redirect(url_for("public.index"))

    hash_matches = meeting.get_mail_signin_hash(meeting_fake_id, expiration) == h
    if not hash_matches:
        flash(_("Lien invalide"), "error")
        return redirect(url_for("public.index"))

    is_expired = datetime.fromtimestamp(float(expiration)) < datetime.now()
    if is_expired:
        flash(_("Lien expiré"), "error")
        return redirect(url_for("public.index"))

    return render_template(
        "meeting/joinmail.html",
        meeting=meeting,
        meeting_fake_id=meeting.fake_id,
        expiration=expiration,
        user_id="fakeuserId",
        h=h,
        role="moderator",
    )


@bp.route("/meeting/signin/<meeting_fake_id>/creator/<int:user_id>/hash/<h>")
def signin_meeting(meeting_fake_id, user_id, h):
    meeting = get_meeting_from_meeting_id_and_user_id(meeting_fake_id, user_id)
    wordings = current_app.config["WORDINGS"]
    if meeting is None:
        flash(
            _(
                "Aucune %(meeting_label)s ne correspond à ces paramètres",
                meeting_label=wordings["meeting_label"],
            ),
            "success",
        )
        return redirect(url_for("public.index"))

    current_user_id = get_current_user().id if has_user_session() else None
    role = meeting.get_role(h, current_user_id)

    if role == "authenticated":
        return redirect(
            url_for(
                "meetings.join_meeting_as_authenticated", meeting_id=meeting_fake_id
            )
        )
    elif not role:
        return redirect(url_for("public.index"))

    return render_template(
        "meeting/join.html",
        meeting=meeting,
        meeting_fake_id=meeting_fake_id,
        user_id=user_id,
        h=h,
        role=role,
    )


@bp.route("/meeting/auth/<meeting_fake_id>/creator/<int:user_id>/hash/<h>")
@auth.oidc_auth("default")
def authenticate_then_signin_meeting(meeting_fake_id, user_id, h):
    return redirect(
        url_for(
            "meetings.signin_meeting",
            meeting_fake_id=meeting_fake_id,
            user_id=user_id,
            h=h,
        )
    )


@bp.route(
    "/meeting/wait/<meeting_fake_id>/creator/<int:user_id>/hash/<h>/fullname/fullname_suffix/",
)
@bp.route(
    "/meeting/wait/<meeting_fake_id>/creator/<int:user_id>/hash/<h>/fullname/<path:fullname>/fullname_suffix/",
)
@bp.route(
    "/meeting/wait/<meeting_fake_id>/creator/<int:user_id>/hash/<h>/fullname/fullname_suffix/<path:fullname_suffix>",
)
@bp.route(
    "/meeting/wait/<meeting_fake_id>/creator/<int:user_id>/hash/<h>/fullname/<path:fullname>/fullname_suffix/<path:fullname_suffix>",
)
def waiting_meeting(meeting_fake_id, user_id, h, fullname="", fullname_suffix=""):
    meeting = get_meeting_from_meeting_id_and_user_id(meeting_fake_id, user_id)
    if meeting is None:
        return redirect(url_for("public.index"))

    current_user_id = get_current_user().id if has_user_session() else None
    role = meeting.get_role(h, current_user_id)
    if not role:
        return redirect(url_for("public.index"))

    return render_template(
        "meeting/wait.html",
        meeting=meeting,
        meeting_fake_id=meeting_fake_id,
        user_id=user_id,
        h=h,
        role=role,
        fullname=fullname,
        fullname_suffix=fullname_suffix,
    )


@bp.route("/meeting/join", methods=["POST"])
def join_meeting():
    form = JoinMeetingForm(request.form)
    if not form.validate():
        return redirect(url_for("public.index"))

    fullname = form["fullname"].data
    meeting_fake_id = form["meeting_fake_id"].data
    user_id = form["user_id"].data
    h = form["h"].data
    meeting = get_meeting_from_meeting_id_and_user_id(meeting_fake_id, user_id)
    if meeting is None:
        return redirect(url_for("public.index"))

    current_user_id = get_current_user().id if has_user_session() else None
    role = meeting.get_role(h, current_user_id)
    fullname_suffix = form["fullname_suffix"].data
    if role == "authenticated":
        fullname = get_authenticated_attendee_fullname()
    elif not role:
        return redirect(url_for("public.index"))

    return redirect(
        meeting.get_join_url(
            role, fullname, fullname_suffix=fullname_suffix, create=True
        )
    )


@bp.route("/meeting/joinmail", methods=["POST"])
def join_mail_meeting():
    form = JoinMailMeetingForm(request.form)
    if not form.validate():
        flash("Lien invalide", "error")
        return redirect(url_for("public.index"))

    fullname = form["fullname"].data
    meeting_fake_id = form["meeting_fake_id"].data
    form["user_id"].data
    expiration = form["expiration"].data
    h = form["h"].data

    meeting = get_mail_meeting(meeting_fake_id)
    if meeting is None:
        flash(
            _(
                "%(meeting_label)s inexistante",
                meeting_label=current_app.config["WORDINGS"][
                    "meeting_label"
                ].capitalize(),
            ),
            "error",
        )
        return redirect(url_for("public.index"))

    hash_matches = meeting.get_mail_signin_hash(meeting_fake_id, expiration) == h
    if not hash_matches:
        flash(_("Lien invalide"), "error")
        return redirect(url_for("public.index"))

    is_expired = datetime.fromtimestamp(expiration) < datetime.now()
    if is_expired:
        flash(_("Lien expiré"), "error")
        return redirect(url_for("public.index"))

    return redirect(meeting.get_join_url("moderator", fullname, create=True))


# Cannot use a flask converter here because sometimes 'meeting_id' is a 'fake_id'
@bp.route("/meeting/join/<int:meeting_id>/authenticated")
@auth.oidc_auth("attendee")
def join_meeting_as_authenticated(meeting_id):
    meeting = db.session.get(Meeting, meeting_id) or abort(404)
    role = "authenticated"
    fullname = get_authenticated_attendee_fullname()
    return redirect(
        url_for(
            "meetings.waiting_meeting",
            meeting_fake_id=meeting_id,
            user_id=meeting.user.id,
            h=meeting.get_hash(role),
            fullname=fullname,
        )
    )


@bp.route("/meeting/join/<meeting:meeting>/<role>")
@auth.oidc_auth("default")
def join_meeting_as_role(meeting, role):
    user = get_current_user()
    if role not in ("attendee", "moderator"):
        abort(404)

    if meeting.user_id == user.id:
        return redirect(meeting.get_join_url(role, user.fullname, create=True))
    else:
        flash(_("Accès non autorisé"), "error")
        return redirect(url_for("public.index"))


@bp.route("/meeting/delete", methods=["POST", "GET"])
@auth.oidc_auth("default")
def delete_meeting():
    if request.method == "POST":
        user = get_current_user()
        meeting_id = request.form["id"]
        meeting = db.session.get(Meeting, meeting_id)

        if meeting.user_id == user.id:
            for meeting_file in meeting.files:
                db.session.delete(meeting_file)
            for meeting_file_external in meeting.externalFiles:
                db.session.delete(meeting_file_external)

            data = meeting.delete_all_recordings()
            return_code = data.get("returncode", "SUCCESS")
            if return_code != "SUCCESS":
                message = data.get("message", "")
                flash(
                    "Nous n'avons pas pu supprimer les vidéos de cette "
                    + current_app.config["WORDINGS"]["meeting_label"]
                    + f" : {message}",
                    "error",
                )
            else:
                db.session.delete(meeting)
                db.session.commit()
                flash(_("Élément supprimé"), "success")
        else:
            flash(_("Vous ne pouvez pas supprimer cet élément"), "error")
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/video/delete", methods=["POST"])
@auth.oidc_auth("default")
def delete_video_meeting():
    user = get_current_user()
    meeting_id = request.form["id"]
    meeting = db.session.get(Meeting, meeting_id)
    if meeting.user_id == user.id:
        recordID = request.form["recordID"]
        data = meeting.delete_recordings(recordID)
        return_code = data.get("returncode")
        if return_code == "SUCCESS":
            flash(_("Vidéo supprimée"), "success")
        else:
            message = data.get("message", "")
            flash(
                _(
                    "Nous n'avons pas pu supprimer cette vidéo : %(code)s, %(message)s",
                    code=return_code,
                    message=message,
                ),
                "error",
            )
    else:
        flash(
            _("Vous ne pouvez pas supprimer cette enregistrement"),
            "error",
        )
    return redirect(url_for("public.welcome"))