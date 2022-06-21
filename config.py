import os
BASE_DIR = os.path.abspath(os.path.dirname(__name__))
DEBUG = True


class Config(object):
   SECRET_KEY = os.environ.get('SECRET_KEY')
   SQLALCHEMY_COMMIT_ON_TEARDOWN = True
   SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'website/app.db')
   DATABASE_CONNECT_OPTIONS = {}
   THREADS_PER_PAGE = 2
   SQLALCHEMY_TRACK_MODIFICATIONS = False
   CSRF_ENABLED     = True
   CSRF_SESSION_KEY = "secret"
