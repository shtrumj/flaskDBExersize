from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from .views import  Myviews


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database/appDb.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] ='False'
    app.register_blueprint(Myviews)
    db.init_app(app)
    return app