from flask import Blueprint, render_template
from flask_login import current_user, login_user, login_required
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/login')
def login():
    return render_template('login.html')


@main.route('/rent')
@login_required
def rent():
    return render_template('rent.html', current_user=current_user)


@main.route('/history')
@login_required
def history():
    return render_template('history.html')


@main.route('/register')
def register():
    return render_template('register.html')


@main.route('/group')
def group():
    return render_template('group.html')
