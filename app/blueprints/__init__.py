from flask import Flask
from .core_bp import core_bp
from .blog_bp import blog_bp


def configure(app: Flask):
    app.register_blueprint(core_bp)
    app.register_blueprint(blog_bp)
