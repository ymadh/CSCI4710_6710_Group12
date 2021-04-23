pip3 install -r requirements.txt
export FLASK_APP=project
export FLASK_DEBUG=1
python3
from project import db, create_app
db.create_all(app=create_app()) 
exit();
flask run
