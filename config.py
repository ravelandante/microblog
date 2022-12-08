import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # uses environment variable if exists, else 'string'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # location of SQL database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # sends a signal to app everytime a change is about to be made to the database (FALSE -> disabled)
    SQLALCHEMY_TRACK_MODIFICATIONS = False