from decouple import config


SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
SQLALCHEMY_TRACK_MODIFICATIONS = False

TEMPLATES_AUTO_RELOAD = config("FLASK_DEBUG", default=False, cast=bool)
