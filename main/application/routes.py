from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect
import sys

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    formData = request.form.get('date')
    formData = str(formData)
    birthDate = requests.post('http://converter:5001/date/' + formData)
    newBirthDate = birthDate.text
    newBirthDate = str(newBirthDate)
    prime = requests.post('http://prime:5002/date/' + newBirthDate)
    print(formData, file=sys.stderr)
    print(formData, file=sys.stdout)
    return render_template('convertPrime.html', formData=formData, birthDate=birthDate, prime=prime)

