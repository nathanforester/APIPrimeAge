from flask import Flask
from application import app
import requests
from flask import url_for, render_template, request

def dob():
    dob = requests.get('http://converter:5001').json()
    return dob

@app.route('/', methods=['GET', 'POST'])
def home():
    date = dob()
    return render_template('months.html', dob=date)

@app.route('/prime/<dob>', methods=['GET', 'POST'])
def prime(dob):
    prime = requests.get('http://primer:5002'+int(dob))
    return render_template('months.html', dob=dob, prime=prime.json()['prime'])