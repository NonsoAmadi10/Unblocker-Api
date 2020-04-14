
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL') or f'sqlite:///{path.join(basedir, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4
 
# Enable the TESTING flag to disable the error catching during request handling
# so that you get better error reports when performing test requests against the application.
    TESTING = True
 
# Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False