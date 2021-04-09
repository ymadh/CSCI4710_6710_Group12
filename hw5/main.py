import psycopg2
from flask import Flask, render_template
import util


app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                              password="pass",
                              host="127.0.0.1",
                              port="5432",
                              database="group12")

# step 1 - all data
cursor = connection.cursor()
allDataQuer = "select * from hw5"
cursor.execute(allDataQuer)
allData = cursor.fetchall()

# step2 - groups based on M / F & age
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

# step 3
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

cursor = connection.cursor()
group3QueryA = "select * from hw5_group3_USA"
cursor.execute(group3QueryA)
group3DataA = cursor.fetchall()
group3QueryB = "select * from hw5_group3_non_USA"
cursor.execute(group3QueryB)
group3DataB = cursor.fetchall()

cursor = connection.cursor()
group4QueryA = "select * from hw5_group4_USA"
cursor.execute(group4QueryA)
group4DataA = cursor.fetchall()
group4QueryB = "select * from hw5_group4_non_USA"
cursor.execute(group4QueryB)
group4DataB = cursor.fetchall()

column_names = ["index", "country", "age", "gender", "fear", "anxious", "angry",
                "happy", "sad", "impact", "fel", "meaning", "occupation"]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alldata')
def alldata():
    labels = ['All Data']
    return render_template('alldata.html',
                           labels_html=labels,
                           column_html=column_names,
                           allData=allData
                           )

@app.route('/step1')
def step1():
    labels = ['Young Male', 'Older Male', 'Young Female', 'Older Female']
    return render_template('step1.html',
                           labels_html=labels,
                           column_html=column_names,
                           group1=group1Data,
                           group2=group2Data,
                           group3=group3Data,
                           group4=group4Data
                           )

@app.route('/step2')
def step2():
    labels = ['Young Male', 'Older Male', 'Young Female', 'Older Female']
    return render_template('step2.html',
                           labels_html=labels,
                           column_html=column_names,
                           group1=group1Data,
                           group2=group2Data,
                           group3=group3Data,
                           group4=group4Data
                           )


@app.route('/step3')
def step3():
    labels = [
        'Young Male USA',
        'Young Male Non-USA',
        'Older Male USA',
        'Older Male Non-USA',
        'Young Female USA',
        'Young Female Non-USA',
        'Older Female USA',
        'Older Female Non-USA']

    data = []
    if (len(group1DataA) > 10):
        label_group = util.cluster_user_data(group1DataA)
        data.append(util.split_user_data(group1DataA, label_group))

    if (len(group1DataB) > 10):
        label_group = util.cluster_user_data(group1DataB)
        data.append(util.split_user_data(group1DataB, label_group))

    if (len(group2DataA) > 10):
        label_group = util.cluster_user_data(group2DataA)
        data.append(util.split_user_data(group2DataA, label_group))

    if (len(group2DataB) > 10):
        label_group = util.cluster_user_data(group2DataB)
        data.append(util.split_user_data(group2DataB, label_group))

    if (len(group3DataA) > 10):
        label_group = util.cluster_user_data(group3DataA)
        data.append(util.split_user_data(group3DataA, label_group))

    if (len(group3DataB) > 10):
        label_group = util.cluster_user_data(group3DataB)
        data.append(util.split_user_data(group3DataB, label_group))

    if (len(group4DataA) > 10):
        label_group = util.cluster_user_data(group4DataA)
        data.append(util.split_user_data(group4DataA, label_group))

    if (len(group4DataB) > 10):
        label_group = util.cluster_user_data(group4DataB)
        data.append(util.split_user_data(group4DataB, label_group))

    return render_template('step3.html',
                           labels_html=labels,
                           column_html=column_names,
                           data=data
                           )


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)
