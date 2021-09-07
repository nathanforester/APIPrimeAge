from flask import Flask, jsonify

from datetime import date

app = Flask(__name__)

@app.route('/')
def dob(BirthYear):
    year = today.year()
    #BirthYear = int(user input)
    ageInMonths = (BirthYear - year) * 12
    return jsonify(ageInMonths) 