from flask import Blueprint, request, render_template, flash

from app.todo.forms import TodoForm
from app.todo.models import Todo


todo = Blueprint('todo', __name__)

@todo.route('/create/', methods=['GET', 'POST'])
def create():
    form = TodoForm(request.form)

    if form.validate_on_submit():
        flash('글 작성 완료')

    flash('글 작성 중 오류 발생')

    return render_template('todo/form.html', form=form)