from flask import Flask
from application import app
import requests
import json
from flask import url_for, render_template, request, redirect, json


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    formData = request.form["date"]
    birthDate = requests.get('http://converter:5001/birthDate/<int:birthDate>' + str(int(formData)))
    prime = requests.get('http://prime:5002/prime/<int:ageInMonths>' + str(int(formData)))
    return render_template('convertPrime.html', formData=formData)

