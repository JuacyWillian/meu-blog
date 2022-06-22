from flask import Flask

from .core_bp import core_bp
from .admin_bp import admin_bp
from .blog_bp import blog_bp
from .shop_bp import shop_bp


def configure(app: Flask):
    app.register_blueprint(core_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(shop_bp)
