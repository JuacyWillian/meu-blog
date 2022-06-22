from flask import Blueprint, redirect, render_template, url_for

from ..utils import posts

shop_bp = Blueprint('shop', __name__, url_prefix='/shop')


@shop_bp.route('/')
def index():
    return render_template('shop/index.html', )
