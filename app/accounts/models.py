from app import db

from app.util.mixins import BaseMixin
from app.util.models import BaseModel

from sqlalchemy.orm import validates


class User(BaseModel, BaseMixin):
    __tablename__ = 'account_user'

    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    @validates('email')
    def validate_email(self, key, value):
        print('validate_email')
        print(key, value)
        assert '@' in value
        return value