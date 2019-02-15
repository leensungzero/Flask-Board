from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


from app.todo.controllers import todo as todo_module
from app.accounts.controllers import account as account_module

app.register_blueprint(todo_module)
app.register_blueprint(account_module)

db.create_all()