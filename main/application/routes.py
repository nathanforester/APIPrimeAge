from flask import Flask
from application import app
import requests
from flask import url_for, render_template, request

def dob():
    birthday = requests.get('http://converter:5001').json()
    return birthday

@app.route('/', methods=['GET', 'POST'])
def home():
    date = birthday()
    return render_template('months.html', birthday=date)

@app.route('/prime/<birthday>', methods=['GET', 'POST'])
def prime(birthday):
    prime = requests.get('http://primer:5002'+int(birthday))
    return render_template('months.html', birthday=birthday, prime=prime.json()['prime'])