from flask import Blueprint, request, render_template, flash, redirect, url_for

from app.todo.forms import TodoForm
from app.todo.model.models import Todo
from app import db

todo = Blueprint('todo', __name__)

@todo.route('/create/', methods=['GET', 'POST'])
def create():
    form = TodoForm(request.form)

    if form.validate_on_submit():
        # Todo: json validator 추가
        # Todo: github 참고 후 exception

        title = request.form['title']
        name = request.form['content']
        todo = Todo.add_todo(title, name)
        flash('글 작성 완료')
        return redirect(url_for('todo.detail', id=todo.id))

    flash('글 작성 중 오류 발생', 'error-message')

    return render_template('todo/form.html', form=form), 200


@todo.route('/', methods=['GET'])
def list():
    query = Todo.get_todo_all()

    todo_list = ([{
        'id': todo.id,
        'title': todo.title,
        'content': todo.content
    } for todo in query])


    return render_template('todo/list.html', todo_list=todo_list), 200


@todo.route('/detail/<int:id>/', methods=['GET', 'POST'])
def detail(id: int):
    todo = Todo.get_todo_by_id(id)

    return render_template('todo/detail.html', todo=todo)


@todo.route('/update/<int:id>/', methods=['GET', 'POST'])
def edit(id: int):
    # Todo: 이 로직 최적화 가능하면 나중에 하기
    if request.method == 'POST':
        form = TodoForm(request.form)

        if form.validate_on_submit():
            title = request.form['title']
            content = request.form['content']

            todo = Todo.get_todo_by_id(id)
            todo.title = title
            todo.content = content

            db.session.commit()

            return redirect(url_for('todo.detail', id=todo.id))
    else:
        todo = Todo.get_todo_by_id(id)

        form = TodoForm(obj=todo)

    return render_template('todo/form.html', form=form)