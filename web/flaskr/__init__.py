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
import logging
import os

from flask import Flask
from flask import request
from flask import session
from flask_babel import Babel
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flaskr.utils import is_rie

from .common.extensions import cache

CRITICAL_VARS = ["OIDC_ISSUER", "OIDC_CLIENT_SECRET", "BIGBLUEBUTTON_SECRET"]
LANGUAGES = ["en", "fr"]


def setup_cache(app):
    cache.init_app(
        app,
        config={
            "CACHE_TYPE": "flask_caching.backends.filesystem",
            "CACHE_DIR": "/tmp/flask-caching",
        },
    )


def setup_logging(app, test_config=None, gunicorn_logging=False):
    if gunicorn_logging:
        gunicorn_logger = logging.getLogger("gunicorn.error")
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    app.config.from_pyfile("config.py")
    if test_config:
        app.config.from_mapping(test_config)


def setup_i18n(app):
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        if request.args.get("lang"):
            session["lang"] = request.args["lang"]
        return session.get("lang", "fr")


def setup_csrf(app):
    csrf = CSRFProtect()
    csrf.init_app(app)


def setup_database(app):
    with app.app_context():
        import flaskr.routes

        app.register_blueprint(flaskr.routes.bp)
        from .models import db

        db.init_app(app)
        Migrate(app, db, compare_type=True)


def setup_jinja(app):
    @app.context_processor
    def global_processor():
        return {
            "config": app.config,
            "beta": app.config["BETA"],
            "documentation_link": app.config["DOCUMENTATION_LINK"],
            "is_rie": is_rie(),
            "version": "1.1.3",
            "LANGUAGES": LANGUAGES,
            **app.config["WORDINGS"],
        }


def setup_error_pages(app):
    from flask import render_template

    @app.errorhandler(400)
    def bad_request(error):
        return render_template("errors/400.html", error=error), 400

    @app.errorhandler(403)
    def not_authorized(error):
        return render_template("errors/403.html", error=error), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html", error=error), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template("errors/500.html", error=error), 500


def create_app(test_config=None, gunicorn_logging=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    setup_cache(app)
    setup_logging(app, test_config, gunicorn_logging)
    setup_i18n(app)
    setup_csrf(app)
    setup_database(app)
    setup_jinja(app)
    setup_error_pages(app)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    return app