from flask import Blueprint, redirect, render_template

from ..utils import posts

admin_bp = Blueprint('admin', import_name=__name__, url_prefix='/admin')

ctx = {"name": "Juacy Willian", "username": "juacywillian"}


@admin_bp.route("/")
def index():
    pass
