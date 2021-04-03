from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/"
db = SQLAlchemy(app)


class HwModel(db.Model):
    __tablename__ = 'public.hw5'

    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, id, country, age, gender, fear, anxious, anger, happy, sad, emotion, meaning, occupation):
        self.id = id
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
        return f"<HW {self.id}>"


# evil gloabl variable...
# the data should be obtained from your db
sample_data = HwModel.query.all()

column_names = ["index", "What country do you live in?", "How old are you?", "What is your gender?", "To what extent do you feel FEAR due to the coronavirus?", "To what extent do you feel ANXIOUS due to the coronavirus?", "To what extent do you feel ANGRY due to the coronavirus?",
                "To what extent do you feel HAPPY due to the coronavirus?", "To what extent do you feel SAD due to the coronavirus?", "Which emotion is having the biggest impact on you?", "What makes you feel that way?", "What brings you the most meaning during the coronavirus outbreak?", "What is your occupation?"]


@app.route('/')
def index():
    labels = util.cluster_user_data(sample_data['user_data'])
    return render_template('index.html', labels_html=labels, column_html=column_names, data_html=sample_data['user_data'])


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
