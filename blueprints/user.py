from flask import Blueprint,render_template

bp = Blueprint('user', __name__, url_prefix = '/')

@bp.route('/login')
def login():
    return render_template('login.html')