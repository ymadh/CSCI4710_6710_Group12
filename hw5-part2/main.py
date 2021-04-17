import os
import json
import util
import psycopg2
import numpy as np
from urllib.parse import unquote
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask import request, jsonify

app = Flask(__name__)

connection = psycopg2.connect(user="postgres",
                              password="pass",
                              host="127.0.0.1",
                              port="5432",
                              database="group12")

# all data


def query_db(query, args=(), one=False):
    cur = connection.cursor()
    cur.execute(query, args)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return (r[0] if r else None) if one else r


cursor = connection.cursor()
allDataQuer = "select * from hw5"
cursor.execute(allDataQuer)
allData = cursor.fetchall()
# country list


def get_country():
    cursor = connection.cursor()
    countryQuery = "select country from hw5 group by country"
    cursor.execute(countryQuery)
    return json.dumps(cursor.fetchall())


# step 1
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

# steps 2 & 3
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
                "happy", "sad", "impact", "feeling", "meaning", "occupation"]


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


@app.route('/api/alldata')
def alldataapi():
    return json.dumps(allData)


@app.route('/api/countries')
def countries():
    return get_country()


@app.route('/api/query_survey_results/<country_name>')
def query_survey_results(country_name):
    country_name = str(country_name)
    decodedCountryName = unquote(country_name)
    if (decodedCountryName == "United States of America"):
    	decodedCountryName = "USA"
    cursor = connection.cursor()
    countryHasDataQuery = "select * from hw5 where country = '" + decodedCountryName + "'"
    # + " and age < 35 and gender = 'Male'"
    cursor.execute(countryHasDataQuery)
    survey_query_data = cursor.fetchall()
    if (len(survey_query_data) > 9):
        label_group = util.cluster_user_data(survey_query_data)
        retData = util.split_user_data(survey_query_data, label_group)
        return json.dumps(retData)
    else:
        return json.dumps([survey_query_data])

@app.route('/api/query_survey_results/<country_name>/<gender>/<age>')
def query_gender_age_results(country_name, gender, age):
    if age == '35 & Under':
        age = 'age <= 35'
    elif age == 'Over 35':
        age = 'age > 35'
    decodedCountryName = unquote(country_name)
    if (decodedCountryName == "United States of America"):
        decodedCountryName = "USA"
    cursor = connection.cursor()
    countryDataQuery = "select * from hw5 where country = '" + decodedCountryName + "' and '" + age + "' and '" + gender + "'"
    survey_results = cursor.fetchall()
    return json.dumps([survey_results])
        
@app.route('/query_survey_results/<country_name>')
def query_survey_country(country_name):
    return render_template('country.html', country_name_html=country_name)


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
    labels = ['Young Male USA',
              'Young Male Non-USA',
              'Older Male USA',
              'Older Male Non-USA',
              'Young Female USA',
              'Young Female Non-USA',
              'Older Female USA',
              'Older Female Non-USA']
    return render_template('step2.html',
                           labels_html=labels,
                           column_html=column_names,
                           group1=group1DataA,
                           group2=group1DataB,
                           group3=group2DataA,
                           group4=group2DataB,
                           group5=group3DataA,
                           group6=group3DataB,
                           group7=group4DataA,
                           group8=group4DataB
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
