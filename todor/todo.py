from flask import Blueprint, render_template, request, redirect, url_for, g

from todor.auth import login_required
from .models import Todo, User
from todor import db

bp = Blueprint('todo', __name__, url_prefix='/todo')


@bp.route('list/')
@login_required
def index():
    """Muestra las tareas del usuario en sesión."""
    todos = Todo.query.all()
    return render_template('todo/index.html', todos=todos)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Crea una tarea nueva asociada al usuario en sesión."""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        todo = Todo(title, description, g.user.id)

        db.session.add(todo)
        db.session.commit()

        return redirect(url_for('todo.index'))
    return render_template('todo/create.html')


def get_todo(id):
    """Obtiene una tarea por id o responde 404 si no existe."""
    todo = Todo.query.get_or_404(id)
    return todo


@bp.route('/update/<int:id>', methods=('GET', 'POST'))
@login_required
def update(id):
    """Edita el título, la descripción y el estado de una tarea."""
    todo = get_todo(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.state = True if request.form.get('state') == 'on' else False

        db.session.commit()

        return redirect(url_for('todo.index'))

    return render_template('todo/update.html', todo=todo)


@bp.route('/delete/<int:id>', methods=('GET', 'POST'))
@login_required
def delete(id):
    """Elimina una tarea."""
    todo = get_todo(id)
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for('todo.index'))


@bp.route('/toggle/<int:id>', methods=('POST',))
@login_required
def toggle(id):
    """Cambia el estado de una tarea entre completada e incompleta."""
    todo = get_todo(id)
    todo.state = not todo.state
    db.session.commit()

    return redirect(url_for('todo.index'))
