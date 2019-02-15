from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from app.util.mixins import BaseMixin
from app.util.models import BaseModel

from sqlalchemy.orm import validates


class User(BaseModel, BaseMixin):
    __tablename__ = 'account_user'

    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, email: str, name: str, password: str):
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)

    def __repr__(self):
        return "<User(email = %s, name = %s, password = %s)" % (self.email, self.name, self.password)

    @validates('email')
    def validate_email(self, key, value):
        print('validate_email')
        print(key, value)
        assert '@' in value
        return value

    def check_password(self, password: str):
        return check_password_hash(self.password, password)

    @staticmethod
    def signup(email: str, name: str, password: str):
        return User(email, name, password).save()
    
    @staticmethod
    def get_user_by_email(email: str):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def signin(email: str, password: str):
        user = User.get_user_by_email(email)

        return user.check_password(password)