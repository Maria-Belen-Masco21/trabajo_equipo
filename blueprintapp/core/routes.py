from flask import Blueprint, redirect, url_for

bp_core = Blueprint(
    'bp_core',
    __name__,
    template_folder='templates'
)

@bp_core.route("/")
def index():
    return redirect(url_for('bp_auth.login'))