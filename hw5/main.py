import json
from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/group12'
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/group12"


class HwModel(db.Model):

    __tablename__ = 'hw5'

    index = db.Column(db.Integer(), primary_key=True)
    country = db.Column(db.String())
    age = db.Column(db.Integer())
    gender = db.Column(db.Integer())
    fear = db.Column(db.Integer())
    anxious = db.Column(db.Integer())
    anger = db.Column(db.Integer())
    happy = db.Column(db.Integer())
    sad = db.Column(db.Integer())
    emotion = db.Column(db.String())
    meaning = db.Column(db.String())
    occupation = db.Column(db.String())

    def __init__(self, index, country, age, gender, fear, anxious, anger, happy, sad, emotion, meaning, occupation):
        self.index = index
        self.country = country
        self.age = age
        self.gender = gender
        self.fear = fear
        self.anxious = anxious
        self.anger = anger
        self.happy = happy
        self.sad = sad
        self.emotion = emotion
        self.meaning = meaning
        self.occupation = occupation

    def __repr__(self):

        return f"<HW {self.index}>"


def parse_data(query_result):
	'''
	this function jsonifies query results
	'''
	result_list = []
	for element in query_result:
		result_list.append([element.index, element.country, element.age, element.gender, element.fear, element.anxious, element.anger, element.happy, element.sad, element.emotion, element.meaning, element.occupation])
	#print({'user_data': result_list})
	return {'user_data': result_list}

# evil gloabl variable...
# the data should be obtained from your db
data = parse_data(HwModel.query.all())

column_names = ["index", "What country do you live in?", "How old are you?", "What is your gender?", "To what extent do you feel FEAR due to the coronavirus?", "To what extent do you feel ANXIOUS due to the coronavirus?", "To what extent do you feel ANGRY due to the coronavirus?",
                "To what extent do you feel HAPPY due to the coronavirus?", "To what extent do you feel SAD due to the coronavirus?", "Which emotion is having the biggest impact on you?", "What makes you feel that way?", "What brings you the most meaning during the coronavirus outbreak?", "What is your occupation?"]


@app.route('/')
def index():
    labels = util.cluster_user_data(data)
    return render_template('index.html', labels_html=labels, column_html=column_names, data_html=data)


if __name__ == '__main__': # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
