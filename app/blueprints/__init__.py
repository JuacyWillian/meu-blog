from flask import Flask
from .core_bp import core_bp


def configure(app:Flask):
    app.register_blueprint(core_bp)