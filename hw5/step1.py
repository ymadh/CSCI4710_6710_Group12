import psycopg2
from flask import Flask, render_template
import util


app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                              password="",
                              host="127.0.0.1",
                              port="5432",
                              database="group12")
cursor = connection.cursor()
group1Query = "select * from hw5_group1"
cursor.execute(group1Query)
group1Data = cursor.fetchall()
group2Query = "select * from hw5_group2"
cursor.execute(group2Query)
group2Data = cursor.fetchall()
group3Query = "select * from hw5_group3"
cursor.execute(group3Query)
group3Data = cursor.fetchall()

group4Query = "select * from hw5_group4"
cursor.execute(group4Query)
group4Data = cursor.fetchall()

column_names = ["index", "country", "age", "gender", "fear", "anxious", "angry",
                "happy", "sad", "impact", "fel", "meaning", "occupation"]


@app.route('/')
def index():
    labels = ['Group1', 'Group2', 'Group3', 'Group4']
    return render_template('index2.html',
                           labels_html=labels,
                           column_html=column_names,
                           group1=group1Data,
                           group2=group2Data,
                           group3=group3Data,
                           group4=group4Data
                           )


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
