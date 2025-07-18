import datetime
import threading
import time
import uuid
import wsgiref
from pathlib import Path

import portpicker
import pytest
from flask_migrate import Migrate
from flask_webtest import TestApp
from jinja2 import FileSystemBytecodeCache
from wsgidav.fs_dav_provider import FilesystemProvider
from wsgidav.wsgidav_app import WsgiDAVApp

import b3desk.utils
from b3desk import create_app
from b3desk.models import db

b3desk.utils.secret_key = lambda: "AZERTY"


@pytest.fixture
def iam_user(iam_server):
    iam_user = iam_server.random_user(
        id="user_id",
        emails=["alice@domain.tld"],
        given_name="Alice",
        user_name="Alice_user_name",
        family_name="Cooper",
    )
    iam_user.save()

    yield iam_user
    iam_user.delete()


@pytest.fixture
def iam_user_2(iam_server):
    iam_user_2 = iam_server.random_user(
        id="user_id2",
        emails=["berenice@domain.tld"],
        given_name="Berenice",
        user_name="Berenice_user_name",
        family_name="Cooler",
    )
    iam_user_2.save()

    yield iam_user_2
    iam_user_2.delete()


@pytest.fixture
def iam_client(iam_server):
    iam_client = iam_server.models.Client(
        client_id="client_id",
        client_secret="client_secret",
        redirect_uris=["http://localhost:5000/oidc_callback"],
        token_endpoint_auth_method="client_secret_post",
        post_logout_redirect_uris=["http://localhost:5000/logout"],
        grant_types=["authorization_code"],
        response_types=["code", "token", "id_token"],
        scope=["openid", "profile", "email"],
        preconsent=True,
    )
    iam_client.save()
    iam_client.audience = [iam_client]
    iam_client.save()
    yield iam_client
    iam_client.delete()


@pytest.fixture
def iam_token(iam_server, iam_client, iam_user):
    iam_token = iam_server.random_token(
        client=iam_client,
        subject=iam_user,
    )
    yield iam_token
    iam_token.delete()


@pytest.fixture
def configuration(tmp_path, iam_server, iam_client, smtpd):
    smtpd.config.use_starttls = True
    return {
        "SECRET_KEY": "test-secret-key",
        "SERVER_NAME": "localhost:5000",
        "PREFERRED_URL_SCHEME": "http",
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
        "TESTING": True,
        "BIGBLUEBUTTON_ENDPOINT": "https://bbb.test",
        "OIDC_ISSUER": iam_server.url,
        "OIDC_REDIRECT_URI": iam_client.redirect_uris[0],
        "OIDC_CLIENT_ID": iam_client.client_id,
        "OIDC_CLIENT_SECRET": iam_client.client_secret,
        "OIDC_CLIENT_AUTH_METHOD": iam_client.token_endpoint_auth_method,
        "OIDC_SCOPES": iam_client.scope,
        "OIDC_USERINFO_HTTP_METHOD": "GET",
        "SECONDARY_IDENTITY_PROVIDER_ENABLED": False,
        "UPLOAD_DIR": str(tmp_path),
        "TMP_DOWNLOAD_DIR": str(tmp_path),
        "RECORDING": True,
        "BIGBLUEBUTTON_ANALYTICS_CALLBACK_URL": "https://bbb-analytics-staging.osc-fr1.scalingo.io/v1/post_events",
        "MEETING_KEY_WORDING": "seminaire",
        "QUICK_MEETING_LOGOUT_URL": "http://education.gouv.fr/",
        "FORCE_HTTPS_ON_EXTERNAL_URLS": False,
        "NC_LOGIN_API_URL": "http://tokenmock:80/index.php",
        "NC_LOGIN_API_KEY": "MY-TOTALLY-COOL-API-KEY",
        "FILE_SHARING": True,
        # Overwrite the web.env values for tests running in docker
        "STATS_URL": None,
        "CACHE_TYPE": "SimpleCache",
        # Disable cache in unit tests
        "CACHE_DEFAULT_TIMEOUT": 0,
        "BIGBLUEBUTTON_API_CACHE_DURATION": 0,
        "MEETING_LOGOUT_URL": "https://example.org/logout",
        "MAIL_MEETING": True,
        "SMTP_FROM": "from@example.org",
        "SMTP_HOST": smtpd.hostname,
        "SMTP_PORT": smtpd.port,
        "SMTP_SSL": smtpd.config.use_ssl,
        "SMTP_STARTTLS": smtpd.config.use_starttls,
        "SMTP_USERNAME": smtpd.config.login_username,
        "SMTP_PASSWORD": smtpd.config.login_password,
        "BIGBLUEBUTTON_DIALNUMBER": "+33bbbphonenumber",
        "ENABLE_PIN_MANAGEMENT": True,
        "ENABLE_SIP": True,
        "FQDN_SIP_SERVER": "example.serveur.com",
        "PRIVATE_KEY": """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPqUq5kkoF9Aj8
rb5F1sfi+x0X5ATa557QE8xcWLiQIJCFTmlaQ+yy0KPAFUy0N1tt2wMe3Z12Zqfk
mF63ixiwkcD6rRre3cMb11XciAM8jFnqZJKyjWd9pGwPmXNO8TGlTxHO7T0VA8L2
TjdYzqPGCTH9ggrGm+z0SMalbaKqwF98FIlLVz9RpTwC+wrbY7u6cNILhc08lTA4
AXgy4QnpJNcxfVXrkg9E4OYrEyNgON/qKBt6AaU1wQ0UR6hmceGW79rZeBLPLR74
Fl6dip5KhuLAOPWQOLNKCJDejzILaKFCZGpWDMLAyr4NKMgXLLmr7cW5Vaw+k2qi
q7Suub6tAgMBAAECggEAH1oRWJQQDfcKlk+K7xNeyVOdUFqSKxSWIxciHv0cHFJ2
T1IH0ON5bIPYfSsaEglbienrfjD6UYJtLbOddTuQZjQTPSV+bZBwoRbxNSLpzi3o
c11s0n1L1ynIUNCbmpsKokkeSK4Dr1UKjdJAQ+2qxz7jJ8GG6/Zln3oPV7GGQh4U
OwPzLI/zBYPeIB+4uMQPshpIHkw7WYEEQuZS0BtoQUkBVDd0KN8YAK0hQlfcQTC/
tXnqcXNCMfKOi01yNiKKBiW0dI2kjW92d5OahdWxdI0ElBjTJ7p5akqpEEYBpbkv
bOk1ytL6jT+yfZ6Q3Pg6ormE4VTUAtZy87tnc+efEQKBgQD91CP/YFbgMBCXWnfI
1MQXiSgZPzHwR8mHW51MvwAIcnBL5Cyl0E0KHuKsyL1DboXFXPAblhCsLcr7g7Q+
nCAedrJ1PamBP5hQCXJVelF9LCnMafKUK/+/vp9tlLhSwevYlitasT5XmDHiFP2t
SvP4GRJDsCNHfq5wG0u27nZNaQKBgQDRcAyhwnSQnTeqQo0lN3bkeDpyfIAdcEB4
GwBsibJzbdmXXbLJ13nUgBD71UKSLoBAxeqGa5nXgeGJ4/2R050+EcVbTfPf6kP/
JTsa9zUpzjxax+ylgCzC73JQRTF+isg9D0zFYzLLwyfdp+izwfyPWv5lGdPo2kXg
2F+9mp3KpQKBgQDlqCtpxCDWdqaMSq5WZyuEn/RH44WrgUg10A5ige3ltqUkBS7g
V7dckNVGv9l+SWF/ULduPjiXkFc3edJ7U4c8COkuarwS1RdaUzG/ZQyV1H99E98H
cUfUlQRqgUTEm/Bn5ncTd4qQdoOrqpJbWJWkxApic9t3tIbfp9K5kMg5AQKBgGX4
3V2hFSoYMjMmxhw5vhyNYT++2I38ypbv5qvx+z3yXUAysctOq5XIaPyEoC4WkAF5
m6+pEjV4mnyN0jc/Rk8jTekfsj7yi/rdgMKnXG4naQF2WAVYu/KJrSniFrAbGFWK
boGow+Gr+mwUxdtH9xVBY52MDr5QEDfigfMKJgu1AoGAXxgMmTGzoCdf+qA1BfGU
2RqFCGZxCNEQvxUWH7QiqDHXVv3KwSCG4w2pcV3z/TBkP9u2jnRjv6pY+WybsUw8
Bv5MNsMlw30mv0xhyDwa5TvvzBgWcU2xseTBWTKLaGUJ82oTtzG3eFHxZ7GLFlP4
0fJCgDTN52LXjWmEyDeLA1c=
-----END PRIVATE KEY-----
""",
    }


@pytest.fixture(scope="session")
def jinja_cache_directory(tmp_path_factory):
    return tmp_path_factory.mktemp("cache")


@pytest.fixture
def app(configuration, jinja_cache_directory):
    app = create_app(configuration)
    app.jinja_env.bytecode_cache = FileSystemBytecodeCache(jinja_cache_directory)

    with app.app_context():
        Migrate(app, db, compare_type=True)
        db.create_all()

    return app


@pytest.fixture
def client_app(app):
    with app.test_request_context():
        yield TestApp(app)


@pytest.fixture
def meeting(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="meeting",
        maxParticipants=99,
        duration=999,
        moderatorPW="moderator",
        attendeePW="attendee",
        is_favorite=True,
        voiceBridge="111111111",
        last_connection_utc_datetime=datetime.datetime(2023, 1, 1),
        visio_code="911111111",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def meeting_2(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="a meeting",
        maxParticipants=99,
        duration=999,
        moderatorPW="moderator",
        attendeePW="attendee",
        is_favorite=True,
        voiceBridge="111111112",
        last_connection_utc_datetime=datetime.datetime(2024, 1, 1),
        visio_code="911111112",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def meeting_3(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="meeting",
        maxParticipants=99,
        duration=999,
        moderatorPW="moderator",
        attendeePW="attendee",
        voiceBridge="111111113",
        visio_code="911111113",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def shadow_meeting(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="shadow meeting",
        moderatorPW="moderator",
        attendeePW="attendee",
        voiceBridge="555555551",
        is_shadow=True,
        last_connection_utc_datetime=datetime.datetime(2025, 1, 1),
        visio_code="511111111",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def shadow_meeting_2(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="shadow meeting must disappear",
        moderatorPW="moderator",
        attendeePW="attendee",
        voiceBridge="555555552",
        is_shadow=True,
        last_connection_utc_datetime=datetime.datetime(2020, 1, 1),
        visio_code="511111112",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def shadow_meeting_3(client_app, user):
    from b3desk.models.meetings import Meeting

    meeting = Meeting(
        user=user,
        name="shadow meeting must disappear too",
        moderatorPW="moderator",
        attendeePW="attendee",
        voiceBridge="555555553",
        is_shadow=True,
        last_connection_utc_datetime=datetime.datetime(2024, 1, 1),
        visio_code="511111113",
    )
    meeting.save()

    yield meeting


@pytest.fixture
def user(client_app, iam_user):
    from b3desk.models.users import User

    user = User(
        email=iam_user.emails[0],
        given_name=iam_user.given_name,
        family_name=iam_user.family_name,
    )
    user.save()

    yield user


@pytest.fixture
def user_2(client_app, iam_user_2):
    from b3desk.models.users import User

    user_2 = User(
        email=iam_user_2.emails[0],
        given_name=iam_user_2.given_name,
        family_name=iam_user_2.family_name,
    )
    user_2.save()

    yield user_2


@pytest.fixture
def previous_voiceBridge(client_app):
    from b3desk.models.meetings import PreviousVoiceBridge

    previous_voiceBridge = PreviousVoiceBridge(voiceBridge="487604786")
    previous_voiceBridge.save()

    yield previous_voiceBridge


@pytest.fixture
def authenticated_user(client_app, user, iam_token, iam_server, iam_user):
    with client_app.session_transaction() as session:
        session["access_token"] = iam_token.access_token
        session["access_token_expires_at"] = ""
        session["current_provider"] = "default"
        session["id_token"] = ""
        session["id_token_jwt"] = ""
        session["last_authenticated"] = "true"
        session["last_session_refresh"] = time.time()
        session["userinfo"] = {
            "email": "alice@domain.tld",
            "family_name": "Cooper",
            "given_name": "Alice",
            "preferred_username": "alice",
        }
        session["refresh_token"] = ""

    iam_server.login(iam_user)
    iam_server.consent(iam_user)

    yield user


@pytest.fixture
def authenticated_user_2(client_app, user_2, iam_token, iam_server, iam_user_2):
    with client_app.session_transaction() as session:
        session["access_token"] = iam_token.access_token
        session["access_token_expires_at"] = ""
        session["current_provider"] = "default"
        session["id_token"] = ""
        session["id_token_jwt"] = ""
        session["last_authenticated"] = "true"
        session["last_session_refresh"] = time.time()
        session["userinfo"] = {
            "email": "berenice@domain.tld",
            "family_name": "Cooler",
            "given_name": "Berenice",
            "preferred_username": "berenice",
        }
        session["refresh_token"] = ""

    iam_server.login(iam_user_2)
    iam_server.consent(iam_user_2)

    yield user_2


@pytest.fixture
def authenticated_attendee(client_app, user, mocker):
    with client_app.session_transaction() as session:
        session["access_token"] = ""
        session["access_token_expires_at"] = ""
        session["current_provider"] = "attendee"
        session["id_token"] = ""
        session["id_token_jwt"] = ""
        session["last_authenticated"] = "true"
        session["last_session_refresh"] = time.time()
        session["userinfo"] = {
            "email": "bob@domain.tld",
            "family_name": "Dylan",
            "given_name": "Bob",
        }
        session["refresh_token"] = ""

    yield user


@pytest.fixture
def bbb_response(mocker):
    class Response:
        content = """<response><returncode>SUCCESS</returncode><running>true</running></response>"""
        status_code = 200
        text = ""

    yield mocker.patch("requests.Session.send", return_value=Response)


@pytest.fixture(scope="session")
def webdav_server(tmp_path_factory):
    root_path = Path(tmp_path_factory.mktemp("webdav"))
    (root_path / "remote.php" / "dav" / "files" / "alice").mkdir(
        parents=True, exist_ok=True
    )
    provider = FilesystemProvider(root_path, readonly=False, fs_opts={})

    config = {
        "host": "localhost",
        "port": portpicker.pick_unused_port(),
        "provider_mapping": {"/": provider},
        "http_authenticator": {"domain_controller": None},
        "simple_dc": {"user_mapping": {"*": True}},
        "verbose": 4,
        "logging": {
            "enable": True,
            "enable_loggers": [],
        },
    }
    app = WsgiDAVApp(config)

    server = wsgiref.simple_server.make_server("localhost", config["port"], app)

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    try:
        yield app
    finally:
        server.shutdown()
        server_thread.join()


class CloudTokenResponse:
    def __init__(self, nc_locator):
        self.data = {
            "nctoken": str(uuid.uuid4()),
            "nclocator": nc_locator,
            "nclogin": "alice",
        }

    def json(self):
        return self.data


@pytest.fixture(autouse=True)
def nextcloud_credentials(mocker, webdav_server):
    response = CloudTokenResponse(
        nc_locator=f"http://{webdav_server.config['host']}:{webdav_server.config['port']}",
    ).data
    mocker.patch(
        "b3desk.models.users.make_nextcloud_credentials_request", return_value=response
    )
    return response


@pytest.fixture
def cloud_service_response(mocker, webdav_server, request):
    scheme = "http://"
    if "secure" in request.keywords:
        scheme = "https://"
    elif "no_scheme" in request.keywords:
        scheme = ""
    return CloudTokenResponse(nc_locator=f"{scheme}cloud-auth-serv.ice")


@pytest.fixture
def jpg_file_content():
    return b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H\x00H\x00\x00\xff\xdb\x00C\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xc2\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00\xff\xc4\x00\x14\x10\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xda\x00\x08\x01\x01\x00\x01?\x10"


class ValidToken:
    def raise_for_status():
        pass

    def json():
        return {"access_token": "valid_token"}


@pytest.fixture
def valid_secondary_identity_token(mocker):
    mocker.patch(
        "b3desk.models.users.get_secondary_identity_provider_token",
        return_value=ValidToken,
    )
