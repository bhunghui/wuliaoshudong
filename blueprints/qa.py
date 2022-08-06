from flask import Blueprint
from flask import render_template
bp = Blueprint('qa', __name__, url_prefix = '/')

@bp.route('/')
def index():

    return render_template('index.html')