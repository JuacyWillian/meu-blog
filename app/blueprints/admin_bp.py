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
@admin_bp.route('/post_list', methods=['GET', 'POST'])
def post_list():
    return render_template('admin/post_list.html')


@admin_bp.route('/post_new', methods=['GET', 'POST'])
def post_new():
    return render_template('admin/post_new.html')


@admin_bp.route('/post_edit/<int:id>', methods=['GET', 'POST'])
def post_edit(id: int):
    return render_template('admin/post_edit.html')


@admin_bp.route('/post_remove/<int:id>', methods=['POST'])
def post_remove(id: int):
    return redirect(url_for('admin.post_list'))


# CATEGORY
@admin_bp.route('/category_list', methods=['GET', 'POST'])
def category_list():
    return render_template('admin/category_list.html')


@admin_bp.route('/category_new', methods=['GET', 'POST'])
def category_new():
    return render_template('admin/category_new.html')


@admin_bp.route('/category_edit/<int:id>', methods=['GET', 'POST'])
def category_edit(id: int):
    return render_template('admin/category_edit.html')


@admin_bp.route('/category_remove/<int:id>', methods=['POST'])
def category_remove(id: int):
    return redirect(url_for('admin.category_list'))
