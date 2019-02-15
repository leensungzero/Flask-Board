from app import db

from app.util.mixins import BaseMixin
from app.util.models import BaseModel


class Todo(BaseModel, BaseMixin):
    # Todo: author, image 추가 계획

    __tablename__ = 'todo_todo'

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title - %r>' % (self.title)

    @staticmethod
    def add_todo(title: str, content: str):
        return Todo(title, content).save()

    @staticmethod
    def get_todo_all():
        return Todo.query.all()

    @staticmethod
    def get_todo_by_id(id: int):
        return Todo.query.filter_by(id=id).first_or_404()