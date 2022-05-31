from flask import Flask

from . import config, models, blueprints

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    models.configure(app)
    blueprints.configure(app)


    return app