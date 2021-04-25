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
    history_info = History.query.filter_by(user_id=current_user.id).all()
    return render_template('history.html', current_user=current_user, history_info=history_info)


@main.route('/register')
def register():
    return render_template('register.html')


@main.route('/group')
def group():
    return render_template('group.html')


@main.route('/reserve', methods=['POST'])
@login_required
def reserve():

    # make sure there is a scooter chosen
    choosen_scooter = request.form['choice']

    scooter = Scooters.query.filter_by(scooter_id=choosen_scooter).first()

    if choosen_scooter is None or scooter is None:
        return redirect("/rent")

    # assume this is their first rental
    # get a history and set the rental number to an incremented value
    rental_no = 1
    if History.query.filter_by(user_id=current_user.id) == None:
        rental_no = History.query(
            func.max('rental_num').filter_by(user_id=current_user.id)).first() + 1

    # insert a new history record
    newHistory = History(user_id=current_user.id,
                         scooter_id=choosen_scooter,
                         name=current_user.name,
                         returned=False,
                         rental_num=rental_no
                         )

    # mark the scooter as unavailable (first is required here)
    updatedScooter = Scooters.query.filter_by(
        scooter_id=choosen_scooter).first()
    updatedScooter.available = False

    # attach the new
    db.session.add(newHistory)
    db.session.commit()

    return render_template('reserved.html', scooter_name=scooter.scooter_brand)
