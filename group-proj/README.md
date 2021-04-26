To run the application:


pip3 install -r requirements.txt

export FLASK_APP=project

export FLASK_DEBUG=1

# To reset the database - this is not required
python3

from project import db, create_app

db.create_all(app=create_app())

exit();

# after running the app navigate to /init
# End reset database

flask run

# login credentials test@test.com / test
