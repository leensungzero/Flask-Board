from flask import Blueprint, request, render_template, redirect, url_for

from flask_login import login_user

from app import db
from app.accounts.models import User
from app.accounts.forms import SignupForm, SigninForm


account = Blueprint('account', __name__, url_prefix='/account/')

@account.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        User.signup(email, name, password)

        return redirect(url_for('todo.list'))

    return render_template('accounts/signup.html', form=form)


@account.route('/signin/', methods=['GET', 'POST'])
def signin():
    form = SigninForm(request.form)

    if form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']

        login_status = User.signin(email, password)

        if login_status[0]:
            user = login_status[1]
            user.authenticated = True
            db.session.commit()
            login_user(user, remember=True)
            return "login success"
        else:
            return "login failed"

    return render_template('accounts/signin.html', form=form)