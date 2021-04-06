import json
from flask import Flask, render_template
import util
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost/group12'
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
    desc = db.Column(db.String())
    meaning = db.Column(db.String())
    occupation = db.Column(db.String())

    def __init__(self, index, country, age, gender, fear, anxious, anger, happy, sad, emotion, desc, meaning, occupation):
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
        self.desc = description
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
        result_list.append([element.index, element.country, element.age, element.gender, element.fear, element.anxious,
                            element.anger, element.happy, element.sad, element.emotion, element. desc, element.meaning, element.occupation])
    #print({'user_data': result_list})
    return result_list


# evil gloabl variable...
# the data should be obtained from your db
#data = parse_data(HwModel.query.all())
data = parse_data(HwModel.query.all())
column_names = ["index", "country", "age", "gender", "fear", "anxious", "angry",
                "happy", "sad", "impact", "fel", "meaning", "occupation"]


@app.route('/')
def index():
    #labels = util.cluster_user_data(data)
    labels = ['young male', 'middle-aged or old male',
              'young female', 'middle-aged or old female']
    display_info = "Data split by gender and age"
    return render_template('index.html', column_html=column_names, data_html=util.split_data_for_hw(data), labels_html=labels, display_html=display_info)


@app.route('/group1')
def group1():
    group1 = parse_data(HwModel.query.filter(
        and_(HwModel.age <= 35, HwModel.gender == 'Male')).all())
    labels = util.cluster_user_data(group1)
    split_result = util.split_user_data(group1, labels)
    display_info = "Data split by gender and age"
    return render_template('group1.html', column_html=column_names, data_html=split_result, labels_html=labels, display_html=display_info)


if __name__ == '__main__':  # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
