import hashlib
import os
import secrets
from datetime import date
from pathlib import Path

import filetype
import requests
from b3desk.forms import MeetingFilesForm
from b3desk.models import db
from b3desk.models.meetings import Meeting
from b3desk.models.meetings import MeetingFiles
from b3desk.models.meetings import MeetingFilesExternal
from flask import Blueprint
from flask import current_app
from flask import flash
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file
from flask import url_for
from flask_babel import lazy_gettext as _
from sqlalchemy import exc
from webdav3.client import Client as webdavClient
from webdav3.exceptions import WebDavException
from werkzeug.utils import secure_filename

from .. import auth
from ..session import get_current_user


bp = Blueprint("meeting_files", __name__)


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


# called by NextcloudfilePicker when documents should be added to a running room:
@bp.route("/meeting/files/<meeting:meeting>/insertDocuments", methods=["POST"])
@auth.oidc_auth("default")
def insertDocuments(meeting):
    from flask import request

    files_title = request.get_json()
    secret_key = current_app.config["SECRET_KEY"]

    xml_beg = "<?xml version='1.0' encoding='UTF-8'?> <modules>  <module name='presentation'> "
    xml_end = " </module></modules>"
    xml_mid = ""
    # @FIX We ONLY send the documents that have been uploaded NOW, not ALL of them for this meetingid ;)
    for cur_file in files_title:
        id = add_external_meeting_file_nextcloud(cur_file, meeting.id)
        filehash = hashlib.sha1(
            f"{secret_key}-1-{id}-{secret_key}".encode()
        ).hexdigest()
        url = url_for(
            "meetings.ncdownload",
            isexternal=1,
            mfid=id,
            mftoken=filehash,
            _external=True,
        )
        xml_mid += f"<document url='{url}' filename='{cur_file}' />"

    bbb_endpoint = current_app.config["BIGBLUEBUTTON_ENDPOINT"]
    xml = xml_beg + xml_mid + xml_end
    params = {"meetingID": meeting.meetingID}
    request = requests.Request(
        "POST",
        "{}/{}".format(current_app.config["BIGBLUEBUTTON_ENDPOINT"], "insertDocument"),
        params=params,
    )
    pr = request.prepare()
    bigbluebutton_secret = current_app.config["BIGBLUEBUTTON_SECRET"]
    s = "{}{}".format(
        pr.url.replace("?", "").replace(
            current_app.config["BIGBLUEBUTTON_ENDPOINT"] + "/", ""
        ),
        bigbluebutton_secret,
    )
    params["checksum"] = hashlib.sha1(s.encode("utf-8")).hexdigest()
    requests.post(
        f"{bbb_endpoint}/insertDocument",
        headers={"Content-Type": "application/xml"},
        data=xml,
        params=params,
    )
    return jsonify(status=200, msg="SUCCESS")


@bp.route("/meeting/files/<meeting:meeting>/toggledownload", methods=["POST"])
@auth.oidc_auth("default")
def toggledownload(meeting):
    user = get_current_user()
    data = request.get_json()

    if user is None:
        return redirect(url_for("public.welcome"))
    meeting_file = db.session.get(MeetingFiles, data["id"])
    if meeting_file is not None and meeting.user_id == user.id:
        meeting_file.is_downloadable = data["value"]
        meeting_file.save()

        return jsonify(status=200, id=data["id"])
    return redirect(url_for("public.welcome"))


@bp.route("/meeting/files/<meeting:meeting>/default", methods=["POST"])
@auth.oidc_auth("default")
def set_meeting_default_file(meeting):
    user = get_current_user()
    data = request.get_json()

    if meeting.user_id == user.id:
        actual_default_file = meeting.default_file
        if actual_default_file:
            actual_default_file.is_default = False

        meeting_file = MeetingFiles()
        meeting_file = meeting_file.query.get(data["id"])
        meeting_file.is_default = True

        if actual_default_file:
            actual_default_file.save()
        meeting_file.save()

    return jsonify(status=200, id=data["id"])


def removeDropzoneFile(absolutePath):
    os.remove(absolutePath)


# called when a file has been uploaded : send it to nextcloud
def add_meeting_file_dropzone(title, meeting_id, is_default):
    user = get_current_user()
    # should be in /tmp/visioagent/dropzone/USER_ID-TITLE
    DROPZONE_DIR = os.path.join(current_app.config["UPLOAD_DIR"], "dropzone")
    Path(DROPZONE_DIR).mkdir(parents=True, exist_ok=True)
    dropzone_path = os.path.join(DROPZONE_DIR, f"{user.id}-{meeting_id}-{title}")
    metadata = os.stat(dropzone_path)
    if int(metadata.st_size) > int(current_app.config["MAX_SIZE_UPLOAD"]):
        return jsonify(
            status=500,
            isfrom="dropzone",
            msg=f"Fichier {title} TROP VOLUMINEUX, ne pas dépasser 20Mo",
        )

    options = {
        "webdav_root": f"/remote.php/dav/files/{user.nc_login}/",
        "webdav_hostname": user.nc_locator,
        "webdav_verbose": True,
        "webdav_token": user.nc_token,
    }
    try:
        client = webdavClient(options)
        client.mkdir("visio-agents")  # does not fail if dir already exists
        # Upload resource
        nc_path = os.path.join("/visio-agents/" + title)
        kwargs = {
            "remote_path": nc_path,
            "local_path": dropzone_path,
        }
        client.upload_sync(**kwargs)

        meeting_file = MeetingFiles()
        meeting_file.nc_path = nc_path

        meeting_file.title = title
        meeting_file.created_at = date.today()
        meeting_file.meeting_id = meeting_id
    except WebDavException as exception:
        user.disable_nextcloud()
        current_app.logger.warning("WebDAV error: %s", exception)
        return jsonify(
            status=500, isfrom="dropzone", msg="La connexion avec Nextcloud est rompue"
        )

    try:
        # test for is_default-file absence at the latest time possible
        meeting = db.session.get(Meeting, meeting_id)
        if len(meeting.files) == 0 and not meeting.default_file:
            meeting_file.is_default = True
        else:
            meeting_file.is_default = False

        meeting_file.save()
        current_app.config["SECRET_KEY"]
        meeting_file.update()
        # file has been associated AND uploaded to nextcloud, we can safely remove it from visio-agent tmp directory
        removeDropzoneFile(dropzone_path)
        return jsonify(
            status=200,
            isfrom="dropzone",
            isDefault=is_default,
            title=meeting_file.short_title,
            id=meeting_file.id,
            created_at=meeting_file.created_at.strftime(
                current_app.config["TIME_FORMAT"]
            ),
        )
    except exc.SQLAlchemyError as exception:
        current_app.logger.error("SQLAlchemy error: %s", exception)
        return jsonify(status=500, isfrom="dropzone", msg="File already exists")


def add_meeting_file_URL(url, meeting_id, is_default):
    title = url.rsplit("/", 1)[-1]

    # test MAX_SIZE_UPLOAD for 20Mo
    metadata = requests.head(url)
    if not metadata.ok:
        return jsonify(
            status=404,
            isfrom="url",
            msg=f"Fichier {title} NON DISPONIBLE, veuillez vérifier l'URL proposée",
        )

    if int(metadata.headers["content-length"]) > int(
        current_app.config["MAX_SIZE_UPLOAD"]
    ):
        return jsonify(
            status=500,
            isfrom="url",
            msg=f"Fichier {title} TROP VOLUMINEUX, ne pas dépasser 20Mo",
        )

    meeting_file = MeetingFiles()

    meeting_file.title = title
    meeting_file.created_at = date.today()
    meeting_file.meeting_id = meeting_id
    meeting_file.url = url
    meeting_file.is_default = is_default

    requests.get(url)

    try:
        meeting_file.save()
        return jsonify(
            status=200,
            isfrom="url",
            isDefault=is_default,
            title=meeting_file.short_title,
            id=meeting_file.id,
            created_at=meeting_file.created_at.strftime(
                current_app.config["TIME_FORMAT"]
            ),
        )
    except exc.SQLAlchemyError as exception:
        current_app.logger.error("SQLAlchemy error: %s", exception)
        return jsonify(status=500, isfrom="url", msg="File already exists")


def add_meeting_file_nextcloud(path, meeting_id, is_default):
    user = get_current_user()

    options = {
        "webdav_root": f"/remote.php/dav/files/{user.nc_login}/",
        "webdav_hostname": user.nc_locator,
        "webdav_verbose": True,
        "webdav_token": user.nc_token,
    }
    try:
        client = webdavClient(options)
        metadata = client.info(path)
    except WebDavException:
        user.disable_nextcloud()
        return jsonify(
            status=500,
            isfrom="nextcloud",
            msg="La connexion avec Nextcloud semble rompue",
        )
    if int(metadata["size"]) > int(current_app.config["MAX_SIZE_UPLOAD"]):
        return jsonify(
            status=500,
            isfrom="nextcloud",
            msg=f"Fichier {path} TROP VOLUMINEUX, ne pas dépasser 20Mo",
        )

    meeting_file = MeetingFiles()

    meeting_file.title = path
    meeting_file.created_at = date.today()
    meeting_file.meeting_id = meeting_id
    meeting_file.nc_path = path
    meeting_file.is_default = is_default
    current_app.config["SECRET_KEY"]

    try:
        meeting_file.save()
        return jsonify(
            status=200,
            isfrom="nextcloud",
            isDefault=is_default,
            title=meeting_file.short_title,
            id=meeting_file.id,
            created_at=meeting_file.created_at.strftime(
                current_app.config["TIME_FORMAT"]
            ),
        )
    except exc.SQLAlchemyError as exception:
        current_app.logger.error("SQLAlchemy error: %s", exception)
        return jsonify(status=500, isfrom="nextcloud", msg="File already exists")


def add_external_meeting_file_nextcloud(path, meeting_id):
    externalMeetingFile = MeetingFilesExternal()

    externalMeetingFile.title = path
    externalMeetingFile.meeting_id = meeting_id
    externalMeetingFile.nc_path = path

    externalMeetingFile.save()
    return externalMeetingFile.id


@bp.route("/meeting/files/<meeting:meeting>", methods=["POST"])
@auth.oidc_auth("default")
def add_meeting_files(meeting):
    user = get_current_user()

    data = request.get_json()
    is_default = False
    if len(meeting.files) == 0:
        is_default = True
    if meeting.user_id == user.id:
        if data["from"] == "nextcloud":
            return add_meeting_file_nextcloud(data["value"], meeting.id, is_default)
        if data["from"] == "URL":
            return add_meeting_file_URL(data["value"], meeting.id, is_default)
        if data["from"] == "dropzone":
            return add_meeting_file_dropzone(
                secure_filename(data["value"]), meeting.id, is_default
            )
        else:
            return make_response(jsonify("no file provided"), 200)

    return jsonify(status=500, msg="Vous ne pouvez pas modifier cet élément")


# for dropzone multiple files uploading at once
@bp.route("/meeting/files/<meeting:meeting>/dropzone", methods=["POST"])
@auth.oidc_auth("default")
def add_dropzone_files(meeting):
    user = get_current_user()

    if user and meeting.user_id == user.id:
        return upload(user, meeting, request.files["dropzoneFiles"])
    else:
        flash("Traitement de requête impossible", "error")
        return redirect(url_for("public.welcome"))


# for dropzone chunk file by file validation
# shamelessly taken from https://stackoverflow.com/questions/44727052/handling-large-file-uploads-with-flask
def upload(user, meeting_id, file):
    DROPZONE_DIR = os.path.join(current_app.config["UPLOAD_DIR"], "dropzone")
    Path(DROPZONE_DIR).mkdir(parents=True, exist_ok=True)
    save_path = os.path.join(
        DROPZONE_DIR, secure_filename(f"{user.id}-{meeting_id}-{file.filename}")
    )
    current_chunk = int(request.form["dzchunkindex"])

    # If the file already exists it's ok if we are appending to it,
    # but not if it's new file that would overwrite the existing one
    if os.path.exists(save_path) and current_chunk == 0:
        # 400 and 500s will tell dropzone that an error occurred and show an error
        return make_response(("File already exists", 500))

    try:
        with open(save_path, "ab") as f:
            f.seek(int(request.form["dzchunkbyteoffset"]))
            f.write(file.stream.read())
    except OSError:
        return make_response(
            ("Not sure why, but we couldn't write the file to disk", 500)
        )

    total_chunks = int(request.form["dztotalchunkcount"])

    if current_chunk + 1 == total_chunks:
        # This was the last chunk, the file should be complete and the size we expect
        mimetype = filetype.guess(save_path)
        if mimetype.mime not in current_app.config["ALLOWED_MIME_TYPES_SERVER_SIDE"]:
            return make_response(("Filetype not allowed", 500))
        if os.path.getsize(save_path) != int(request.form["dztotalfilesize"]):
            return make_response(("Size mismatch", 500))

    return make_response(("Chunk upload successful", 200))


@bp.route("/meeting/files/delete", methods=["POST"])
@auth.oidc_auth("default")
def delete_meeting_file():
    user = get_current_user()
    data = request.get_json()
    meeting_file_id = data["id"]
    meeting_file = MeetingFiles()
    meeting_file = meeting_file.query.get(meeting_file_id)
    meeting = Meeting()
    cur_meeting = meeting.query.get(meeting_file.meeting_id)

    if cur_meeting.user_id == user.id:
        db.session.delete(meeting_file)
        db.session.commit()
        new_default_id = None
        if meeting_file.is_default:
            cur_meeting = meeting.query.get(meeting_file.meeting_id)
            if len(cur_meeting.files) > 0:
                cur_meeting.files[0].is_default = True
                new_default_id = cur_meeting.files[0].id
                cur_meeting.save()
        return jsonify(
            status=200,
            newDefaultId=new_default_id,
            id=data["id"],
            msg="Fichier supprimé avec succès",
        )
    return jsonify(
        status=500, id=data["id"], msg="Vous ne pouvez pas supprimer cet élément"
    )


# draft for insertDocument calls to BBB API
# @TODO: can we remove this def entirely?
@bp.route("/insertDoc/<token>")
def insertDoc(token):
    # select good file from token
    # get file through NC credentials - HOW POSSIBLE ?
    # return file as response to BBB server

    meeting_file = MeetingFiles.query.filter_by(download_hash=token).one()
    secret_key = current_app.config["SECRET_KEY"]
    if (
        meeting_file
        or meeting_file.token
        != hashlib.sha1(
            f"{secret_key}{meeting_file.id}{secret_key}".encode()
        ).hexdigest()
    ):
        make_response("NOT OK", 500)

    params = {"meetingID": meeting_file.meeting.meetingID}
    action = "insertDocument"
    req = requests.Request(
        "POST",
        "{}/{}".format(current_app.config["BIGBLUEBUTTON_ENDPOINT"], action),
        params=params,
    )
    headers = {"Content-Type": "application/xml"}
    pr = req.prepare()
    bigbluebutton_secret = current_app.config["BIGBLUEBUTTON_SECRET"]
    s = "{}{}".format(
        pr.url.replace("?", "").replace(
            current_app.config["BIGBLUEBUTTON_ENDPOINT"] + "/", ""
        ),
        bigbluebutton_secret,
    )
    params["checksum"] = hashlib.sha1(s.encode("utf-8")).hexdigest()

    # xml now use
    url = url_for(
        "meetings.ncdownload",
        isexternal=0,
        mfid=meeting_file.id,
        mftoken=meeting_file.download_hash,
        _external=True,
    )
    xml = f"<?xml version='1.0' encoding='UTF-8'?> <modules>  <module name='presentation'><document url='{url}' filename='{meeting_file.title}' /> </module></modules>"

    requests.post(
        f"{current_app.config['BIGBLUEBUTTON_ENDPOINT']}/insertDocument",
        data=xml,
        headers=headers,
        params=params,
    )

    return make_response("ok", 200)