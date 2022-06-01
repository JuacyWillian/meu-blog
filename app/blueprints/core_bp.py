from distutils import core
from flask import Blueprint, render_template

core_bp = Blueprint('core', __name__)

@core_bp.route('/')
def index():

    return render_template('index.html', 
        name="Juacy Willian", username="juacywillian")
    