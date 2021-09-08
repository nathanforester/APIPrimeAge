from flask import Flask, jsonify

from datetime import date

app = Flask(__name__)

@app.route('/')
def dob(BirthYear):
    year = datetime.utcnow().year
    #BirthYear = int(user input)
    ageInMonths = (int(year) - BirthYear) * 12
    return jsonify(ageInMonths) 