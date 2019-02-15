from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    email = StringField('아이디', [
        DataRequired(message='아이디는 필수 입력입니다.')
    ])
    name = StringField('사용자 이름', [
        DataRequired(message='사용자 이름은 필수 입력입니다.')
    ])
    password = PasswordField('패스워드', [
        DataRequired(message='패스워드는 필수 입력입니다.')
    ])