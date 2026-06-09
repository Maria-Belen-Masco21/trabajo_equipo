from flask import request, render_template, redirect, url_for, Blueprint
from flask_login import login_required

from blueprintapp.app import db
from blueprintapp.tareas.models import Tarea

bp_tarea = Blueprint('bp_tarea',__name__,template_folder='templates')

@bp_tarea.route("/")
@login_required
def index():
    tareas = Tarea.query.all()
    return render_template('tareas/index.html',tareas=tareas)

@bp_tarea.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        tarea = Tarea(
            descripcion=request.form.get('descripcion'),
            completado=True if 'completado' in request.form else False)

        db.session.add(tarea)
        db.session.commit()

        return redirect(url_for('bp_tarea.index'))

    return render_template('tareas/create.html')

@bp_tarea.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):

    tarea = Tarea.query.get_or_404(id)

    if request.method == 'POST':

        tarea.descripcion = request.form.get('descripcion')
        tarea.completado = True if 'completado' in request.form else False

        db.session.commit()

        return redirect(url_for('bp_tarea.index'))

    return render_template(
        'tareas/edit.html',
        tarea=tarea
    )

@bp_tarea.route('/delete/<int:id>')
@login_required
def delete(id):

    tarea = Tarea.query.get_or_404(id)

    db.session.delete(tarea)
    db.session.commit()

    return redirect(url_for('bp_tarea.index'))