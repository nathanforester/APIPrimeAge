from flask import Flask
from application import app
from flask import url_for, render_template, request, redirect, json, requests

def dob():
    dob = requests.get('http://converter:5001').json()
    return dob

@app.route('/', methods=['GET', 'POST'])
def home():
    date = dob
    if request.method == "POST":
        date = request.form["dob"]
        return redirect(url_for('index.html', dob=date))
    else:
        return render_template('index.html')

@app.route('/prime/<dob>', methods=['GET', 'POST'])
def prime(dob):
    prime = requests.get('http://prime:5002'+int(dob))
    return render_template('convertPrime.html', dob=dob, prime=prime.json()['prime'])