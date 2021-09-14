from flask import Flask
from application import app
import requests
from flask import url_for, render_template, request, redirect, json

def dob():
    dob = requests.get('http://converter:5001').json()
    return dob

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        date = dob
        return redirect(url_for('prime', dob=date))

    return render_template('index.html')

@app.route('/prime/', methods=['GET', 'POST'])
def prime():
    if request.method == 'GET':
        prime = requests.get('http://prime:5002').json()
        return redirect(url_for('prime'))
    else:
        return render_template('convertPrime.html', dob=dob)