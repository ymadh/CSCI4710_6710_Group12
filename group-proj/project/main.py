from flask import Blueprint, render_template, request, redirect
from flask_login import current_user, login_user, login_required
from sqlalchemy import func, insert, update
from . import db
from .models import User
from .models import Scooters
from .models import Renters
from .models import History
from .models import User


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
    rental_info = Scooters.query.filter_by(available=True).all() 

    return render_template('rent.html', current_user=current_user, rental_info=rental_info)

@main.route('/return_scooter')
@login_required
def return_scooter():
    return_info = History.query.filter_by(returned=False).all()
    return render_template('return_scooter.html', current_user=current_user, return_info=return_info)


@main.route('/history')
@login_required
def history():
    current_user = User.query.filter_by(is_active=1).first()
    print(current_user.id)
    history_info = History.query.filter_by(user_id=current_user.id)
    return render_template('history.html', current_user=current_user, history_info=history_info)


@main.route('/register')
def register():
    return render_template('register.html')


@main.route('/group')
def group():
    return render_template('group.html')


@main.route('/reserve')
@login_required
def reserve():
    user = User.query.filter_by(is_active=1).first()
    if History.query.filter_by(user_id=user.id) == None:
        rental_no = History.query(func.max('rental_num')filter_by(user_id=user.id)).first() + 1
    else:
        rental_no = 1
    insert(History).values(user_id=user.id, scooter_id=request.form['id'], name=user.name, returned=false, rental_num=rental_no)
    update(Scooters).where(scooter_id == request.form['id']).values(available=False)
    db.session.commit()

    return render_template('history.html')
