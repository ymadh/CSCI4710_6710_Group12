from flask import Blueprint, render_template, request, redirect, Response
from flask_login import current_user, login_user, login_required
from sqlalchemy import func, insert, update, desc, and_
from . import db
from .models import User
from .models import Scooters
from .models import Renters
from .models import History
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime



main = Blueprint('main', __name__)


@main.route('/init')
def init():
    # create data
    new_user = User(email='test@test.com', name='Test User',
                    password=generate_password_hash('test', method='sha256'), is_active=1)

    # add the new user to the database
    db.session.add(new_user)

    # create scooters
    scooter1 = Scooters(scooter_brand='Chili', available=True, location='A')
    scooter2 = Scooters(scooter_brand='Lime', available=True, location='A')
    scooter3 = Scooters(scooter_brand='Mango', available=True, location='B')
    scooter4 = Scooters(scooter_brand='Suzuki', available=True, location='B')
    scooter5 = Scooters(scooter_brand='Vespa', available=True, location='C')
    scooter6 = Scooters(scooter_brand='Piaggo', available=True, location='C')
    scooter7 = Scooters(scooter_brand='Aprilia', available=True, location='D')
    db.session.add(scooter1)
    db.session.add(scooter2)
    db.session.add(scooter3)
    db.session.add(scooter4)
    db.session.add(scooter5)
    db.session.add(scooter6)
    db.session.add(scooter7)

    db.session.commit()
    return redirect('/')


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
    
    current_status = History.query.filter_by(user_id=current_user.id, return_date=None).count()
    print(current_status)

    return render_template('rent.html', current_user=current_user, rental_info=rental_info, current_status=current_status)


@main.route('/return_scooter')
@login_required
def return_scooter():
    # hackish way b/c null isn't working
    #t = datetime.datetime(2001, 1, 1)

    if History.query.filter_by(
        user_id=current_user.id, return_date=None).first() != None:

        return_info = History.query.filter_by(
            user_id=current_user.id, return_date=None).first()
        
        scooter_info = Scooters.query.filter_by(
            scooter_id=return_info.scooter_id).first()
  
        return render_template('return_scooter.html', current_user=current_user, return_info=return_info, scooter_info=scooter_info, already_renting='Renting')
    else:
        return render_template('return_scooter.html', current_user=current_user, return_info=None, scooter_info=None, already_renting='NotRenting')

@main.route('/returnAPI', methods=['POST'])
@login_required
def returnAPI():
    return_info = History.query.filter_by(
    user_id=current_user.id, return_date=None).first()
       
    return_info.return_date = datetime.datetime.now()

    returnedScooter = Scooters.query.filter_by(
        scooter_id=return_info.scooter_id).first()
    returnedScooter.available = True
    
        
    db.session.commit()
    
    return render_template('return_scooter.html', current_user=current_user, return_info=None, scooter_info=None, already_renting='Returning')

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
    #t = datetime.datetime(2001, 1, 1)

    newHistory = History(user_id=current_user.id,
                         scooter_id=choosen_scooter,
                         rental_num=rental_no,
                         rent_date=datetime.datetime.now()
                         )

    # mark the scooter as unavailable (first is required here)
    updatedScooter = Scooters.query.filter_by(
        scooter_id=choosen_scooter).first()
    updatedScooter.available = False

    # attach the new
    db.session.add(newHistory)
    db.session.commit()

    return render_template('reserved.html', scooter_name=scooter.scooter_brand)
