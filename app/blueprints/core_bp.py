from flask import Blueprint, redirect, render_template, url_for

from ..utils import posts

core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def index():
    return redirect(url_for('blog.index'))


@core_bp.route('/about')
def about():
    return render_template('about.html',
                           name="Juacy Willian", username="juacywillian", posts=posts)


@core_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html',
                           name="Juacy Willian", username="juacywillian", posts=posts)
