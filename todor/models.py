from todor import db


class User(db.Model):
    """Usuario de la aplicación, identificado por un username único."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)  # hash, nunca en texto plano

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


class Todo(db.Model):
    """Tarea de la lista, asociada al usuario que la creó."""
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    state = db.Column(db.Boolean, default=False)  # True = completada

    def __init__(self, title, description, created_by, state=False):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.state = state

    def __repr__(self):
        return f'<Todo {self.title}>'
