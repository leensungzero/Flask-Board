from flask_wtf import FlaskForm

from wtforms import StringField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('제목', [
        DataRequired(message="제목은 필수 입력입니다.")
    ])
    content = StringField('내용', [
        DataRequired(message="내용은 필수 입력입니다.")
    ])