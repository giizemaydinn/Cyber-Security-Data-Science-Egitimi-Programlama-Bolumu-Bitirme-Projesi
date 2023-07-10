from dataclasses import dataclass
from initialize import db

@dataclass
class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120))
    done = db.Column(db.Boolean, default=False)

    def __init__(self, id, description, done):
        self.id = id
        self.description = description
        self.done = done

    @classmethod
    def get_all_todos(cls):
        return cls.query.all()

    @classmethod
    def get_todo_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_todo(cls, description, done):
        todo = cls(None, description, done)
        db.session.add(todo)
        db.session.commit()

    @classmethod
    def update_todo(cls, id, description, done):
        todo = cls.query.filter_by(id=id).first()
        todo.description = description
        todo.done = done
        db.session.commit()

    @classmethod
    def delete_todo(cls, id):
        todo = cls.query.filter_by(id=id).first()
        db.session.delete(todo)
        db.session.commit()