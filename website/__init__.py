from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, Blueprint
from website.views import Myviews
from .dbModel import Base, Users, Sites
from website.database import db


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("../instance/config.py")
    app.register_blueprint(views.Myviews)
    return app


def create_db(app):
        db.create_all()
