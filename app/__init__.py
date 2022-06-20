from flask import Flask
from flaskext.markdown import Markdown


from . import config, models, blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    Markdown(app)
    models.configure(app)
    blueprints.configure(app)

    return app
