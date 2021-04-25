from flask import Blueprint, render_template
from flask_login import current_user, login_user, login_required
#from WTForms import Radiofield
from . import db
from .models import Scooters
from .models import Renters
from .models import History


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
    #radioFields = RadioField('Available Scooters', choices=[(rental_info)])  

    return render_template('rent.html', current_user=current_user, rental_info=rental_info)


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


def connect_db(fileLocation):
    conn = None
    try:
        conn = sqlite3.connect(project/db.sqlite)
    except:
        print('Something went wrong. Please try again.')
    return conn


def query_db(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    return(cur.fetchall())
