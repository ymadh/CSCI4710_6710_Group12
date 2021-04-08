import psycopg2
from flask import Flask, render_template
import util
import numpy as np


app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                              password="",
                              host="127.0.0.1",
                              port="5432",
                              database="group12")
cursor = connection.cursor()
group1QueryA = "select * from hw5_group1_USA"
cursor.execute(group1QueryA)
group1DataA = cursor.fetchall()
group1QueryB = "select * from hw5_group1_non_USA"
cursor.execute(group1QueryB)
group1DataB = cursor.fetchall()

cursor = connection.cursor()
group2QueryA = "select * from hw5_group2_USA"
cursor.execute(group2QueryA)
group2DataA = cursor.fetchall()
group2QueryB = "select * from hw5_group2_non_USA"
cursor.execute(group2QueryB)
group2DataB = cursor.fetchall()

column_names = ["index", "country", "age", "gender", "fear", "anxious", "angry",
                "happy", "sad", "impact", "fel", "meaning", "occupation"]


@app.route('/')
def index():
    labels = ['Group1 - USA', 'Group1 - Non USA',
              'Group2 USA ', 'Group2 - Non USA']

    if (len(group1DataA) > 10):
        labels_group1 = util.cluster_user_data(group1DataA)
        data1 = util.split_user_data(group1DataA, labels_group1)

    return render_template('step2.html',
                           labels_html=labels,
                           column_html=column_names,
                           data1_html=data1,
                           group1DataA_html=group1DataA,
                           group1DataB_html=group1DataB,
                           group2DataA_html=group2DataA,
                           group2DataB_html=group2DataB
                           )


if __name__ == '__main__':
    # set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)
