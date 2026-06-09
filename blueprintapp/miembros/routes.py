from flask import request, render_template, redirect, url_for, Blueprint
from flask_login import login_required

from blueprintapp.app import db
from blueprintapp.miembros.models import Miembro

bp_miembro = Blueprint(
    'bp_miembro',__name__,template_folder='templates')

@bp_miembro.route("/")
@login_required
def index():
    miembros = Miembro.query.all()
    return render_template('miembro/index.html',miembros=miembros)

@bp_miembro.route("/create", methods=['GET', 'POST'])
@login_required
def create():

    if request.method == 'POST':
        miembro = Miembro(
            nombre=request.form.get('nombre'),
            email=request.form.get('email'))

        db.session.add(miembro)
        db.session.commit()

        return redirect(url_for('bp_miembro.index'))

    return render_template('miembro/create.html')

@bp_miembro.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):

    miembro = Miembro.query.get_or_404(id)

    if request.method == 'POST':

        miembro.nombre = request.form.get('nombre')
        miembro.email = request.form.get('email')

        db.session.commit()

        return redirect(url_for('bp_miembro.index'))

    return render_template(
        'miembro/edit.html',
        miembro=miembro
    )

@bp_miembro.route('/delete/<int:id>')
@login_required
def delete(id):

    miembro = Miembro.query.get_or_404(id)

    db.session.delete(miembro)
    db.session.commit()

    return redirect(url_for('bp_miembro.index'))