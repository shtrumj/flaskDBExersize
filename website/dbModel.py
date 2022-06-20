from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()


class Base(db.Model):
    __abstract__= True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


class Users(Base):
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(80))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


class Sites(Base):
    name = db.Column(db.String)
    domain = db.Column(db.String)

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain


