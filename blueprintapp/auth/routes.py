from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from blueprintapp.app import User

bp_auth = Blueprint('bp_auth', __name__,template_folder='templates')

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        print("Usuario:", usuario)
        print("Password:", password)
        if usuario == 'admin' and password == '1234':
            user = User(1)
            login_user(user)
            return redirect(url_for('bp_miembro.index'))
        else:
            print("Usuario o contraseña incorrectos")
    return render_template('auth/login.html')

@bp_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('bp_auth.login'))