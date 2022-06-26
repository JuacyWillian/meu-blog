from flask import Blueprint, redirect, render_template

from ..utils import posts

blog_bp = Blueprint('blog', import_name=__name__, url_prefix='/blog')

ctx = {"name": "Juacy Willian", "username": "juacywillian"}


@blog_bp.route('/')
def index():
    ctx["posts"] = posts

    return render_template(
        'blog/index.html',
        **ctx,
    )


@blog_bp.route('/view_post/<int:id>')
def view_post(id):
    ctx["post"] = posts[id-1]

    return render_template(
        'blog/view_post.html',
        **ctx
    )
