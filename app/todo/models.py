from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Todo(Base):
    # Todo: author, image 추가 계획

    __tablename__ = 'todo_todo'

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(2000), nullable=False)

    def __int__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return '<Title - %r>' % (self.title)