from flask import Flask
from application import app
import requests
import json
from flask import url_for, render_template, request, redirect, json


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/prime', methods=['GET', 'POST'])
def prime():
    return render_template('convertPrime.html')

@app.route('/date', methods=['GET', 'POST'])
def date():
    if requests.get=="POST":
        birthDate = requests.post('http://converter:5001/birthDate')
        prime = requests.post('http://prime:5002/prime')
        formData = request.form["date"]
        return redirect(url_for("prime", birthDate=formData))
    
    return render_template("index.html")

