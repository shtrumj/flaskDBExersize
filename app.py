from flask_sqlalchemy import SQLAlchemy

import website.views
from website import create_app, create_db
from flask import Blueprint, Flask


if __name__ == '__main__':
    app = create_app()
    create_db(app)
    app.run(host='0.0.0.0', debug=True)
