from flask import Blueprint, request, render_template, flash

from app.todo.forms import TodoForm
from app.todo.model.models import Todo

todo = Blueprint('todo', __name__)

@todo.route('/create/', methods=['GET', 'POST'])
def create():
    form = TodoForm(request.form)

    if form.validate_on_submit():
        # Todo: json validator 추가
        # Todo: github 참고 후 exception

        title = request.form['title']
        name = request.form['content']
        Todo.add_todo(title, name)
        flash('글 작성 완료')
        return 'success'

    flash('글 작성 중 오류 발생', 'error-message')

    return render_template('todo/form.html', form=form)