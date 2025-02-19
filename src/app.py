"""
app.py

Type `flask run` command to run the application
"""

from http.client import HTTPException
from flask import Flask, jsonify, redirect
from flask_injector import FlaskInjector

from config import Config
from src.server.commands import db_seed, migration_fresh
from src.server.configs import login_manager
from src.server.configs.db import db
from src.server.configs.ioc_container import configure
from src.server.models.user import User


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="client/templates")
    app.config.from_object(config_class)

    # Database Configuration
    db.init_app(app)

    ###############################
    # Client Blueprints
    ###############################
    from src.client.routes.index import index_bp
    from src.client.routes.auth import auth_bp

    app.register_blueprint(index_bp, url_prefix="/")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    ###############################
    # Server Blueprints
    ###############################
    from src.server.routes.users import users_bp
    from src.server.routes.questions import questions_bp
    from src.server.routes.exams import exams_bp
    from src.server.routes.scores import scores_bp
    from src.server.routes.auth import auth_api_bp

    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(questions_bp, url_prefix="/api/questions")
    app.register_blueprint(exams_bp, url_prefix="/api/exams")
    app.register_blueprint(scores_bp, url_prefix="/api/scores")
    app.register_blueprint(auth_api_bp, url_prefix="/api/auth")

    # Commands
    app.cli.add_command(migration_fresh)
    app.cli.add_command(db_seed)

    # Authentication
    login_manager.login_manager.init_app(app)

    @login_manager.login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    FlaskInjector(app=app, modules=[configure])

    # Exception Handling
    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        redirect("/")
        return jsonify(error=str(e)), code

    return app
