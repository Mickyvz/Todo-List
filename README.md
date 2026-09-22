# Todo List

Aplicación web de lista de tareas hecha con Flask. Permite registrarse, iniciar sesión y gestionar tareas propias (crear, editar, marcar como completadas y eliminar).

## Tecnologías

- Python + Flask
- Flask-SQLAlchemy (SQLite)
- Bootstrap 5

## Instalación

```bash
git clone <url-del-repo>
cd Todo-List
python -m venv env-todo
env-todo\Scripts\activate      # Windows
pip install -r requirements.txt
```

## Uso

```bash
python run.py
```

La aplicación queda disponible en `http://127.0.0.1:5000`. La base de datos SQLite se crea automáticamente en `instance/todolist.db` la primera vez que se ejecuta.

## Estructura del proyecto

```
todor/
├── __init__.py      # Application factory, configuración y registro de blueprints
├── auth.py          # Registro, login, logout y protección de rutas
├── todo.py          # CRUD de tareas
├── models.py        # Modelos User y Todo
└── templates/        # Plantillas Jinja2
run.py                # Punto de entrada de la aplicación
```
