from flask import Flask
from application import app
import requests
from flask import render_template, request, redirect


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/date', methods=['GET', 'POST'])
def date():
    formData = request.values.get('date')
    birthDate = requests.post(f'http://converter:5001/birthDate/{formData}')
    prime = requests.post(f'http://prime:5002/prime/{formData}')
    return render_template('convertPrime.html', formData=formData, birthDate=birthDate, prime=prime)

