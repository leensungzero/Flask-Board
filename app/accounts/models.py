from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from app.util.mixins import BaseMixin
from app.util.models import BaseModel

from sqlalchemy.orm import validates

from app import login_manager


class User(BaseModel, BaseMixin):
    __tablename__ = 'account_user'

    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    authenticated = db.Column(db.Boolean, nullable=False)

    def __init__(self, email: str, name: str, password: str, authenticated=False):
        self.email = email
        self.name = name
        self.password = generate_password_hash(password)
        self.authenticated = authenticated

    def __repr__(self):
        return "<User(email = %s, name = %s, password = %s)" % (self.email, self.name, self.password)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    @validates('email')
    def validate_email(self, key, value):
        print('validate_email')
        print(key, value)
        assert '@' in value
        return value

    def check_password(self, password: str):
        print(self.password)
        print(password)
        return check_password_hash(self.password, password)

    @staticmethod
    def signup(email: str, name: str, password: str):
        return User(email, name, password).save()

    @staticmethod
    @login_manager.user_loader
    def get_user_by_email(email: str):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def signin(email: str, password: str):
        user = User.get_user_by_email(email)

        return (user.check_password(password), user)