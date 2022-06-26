from flask import Blueprint, redirect, render_template, url_for

from ..utils import posts

admin_bp = Blueprint('admin', import_name=__name__, url_prefix='/admin')

ctx = {"name": "Juacy Willian", "username": "juacywillian"}


@admin_bp.route("/")
def index():
    return render_template('admin/index.html')


@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('admin/login.html')


@admin_bp.route('/logout')
def logout():
    return redirect(url_for('core.index'))


# POST
@admin_bp.route('/all_posts', methods=['GET', 'POST'])
def all_posts():
    return render_template('admin/all_posts.html')


@admin_bp.route('/new_post', methods=['GET', 'POST'])
def new_post():
    return render_template('admin/new_post.html')


@admin_bp.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id: int):
    return render_template('admin/edit_post.html')


@admin_bp.route('/remove_post/<int:id>', methods=['POST'])
def remove_post(id: int):
    return redirect(url_for('admin.all_post'))


# CATEGORY
@admin_bp.route('/all_category', methods=['GET', 'POST'])
def all_category():
    return render_template('admin/all_category.html')


@admin_bp.route('/new_category', methods=['GET', 'POST'])
def new_category():
    return render_template('admin/new_category.html')


@admin_bp.route('/edit_category/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    return render_template('admin/edit_category.html')


@admin_bp.route('/remove_category/<int:id>', methods=['POST'])
def remove_category(id: int):
    return redirect(url_for('admin.all_category'))
