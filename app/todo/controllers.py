from flask import Blueprint, request, render_template, flash

from app.todo.forms import TodoForm
from app.todo.model.models import Todo

import json

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
        return 'success', 200

    flash('글 작성 중 오류 발생', 'error-message')

    return render_template('todo/form.html', form=form), 200


@todo.route('/', methods=['GET'])
def list():
    query = Todo.get_todo_all()
    print(query)

    todo_list = ([{
        'title': todo.title,
        'content': todo.content
    } for todo in query])


    return render_template('todo/list.html', todo_list=todo_list), 200


@todo.route('/detail/<int:id>/', methods=['GET', 'POST'])
def detail(id):
    obj = Todo.get_todo_by_id(id)
    print(obj)

    return obj.titled