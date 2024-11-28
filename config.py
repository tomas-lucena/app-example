import urllib.parse

class Default:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5101
    SECRET_KEY = 'SECRET_KEY'

class Development(Default):
    FLASK_ENV="development"
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:0400@localhost:5432/hexa'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database-postgres:5432/db'
    HOST = '0.0.0.0'
    DEBUG = True

class Production(Default):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database-postgres.nextzen.com:5432/db'
    HOST = '0.0.0.0'
    DEBUG = False
