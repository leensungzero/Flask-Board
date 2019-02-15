from flask import Blueprint, request, render_template

from app import db
from app.accounts.models import User
from app.accounts.forms import SignupForm


account = Blueprint('account', __name__, url_prefix='/account/')

@account.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)

    if form.validate_on_submit():
        email = request.form['email']
        name = request.form['name']
        password = request.form['password']

        user = User.signup(email, name, password)

        return user.name

    return render_template('accounts/signup.html', form=form)