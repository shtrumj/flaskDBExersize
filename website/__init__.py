from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy
from .extensions import db
from .views import Myviews
from flask_migrate import Migrate


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database/appDb.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] ='False'
    app.config['SECRET_KEY'] = '4bafa7a5ae1d045970fba2b6'
    app.register_blueprint(Myviews)
    db.init_app(app)
    Migrate(app,db)
    return app