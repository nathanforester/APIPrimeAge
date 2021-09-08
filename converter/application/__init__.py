from flask import Flask, jsonify

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def dob(BirthYear):
    year = datetime.utcnow().year
    ageInMonths = (int(year) - BirthYear) * 12
    return jsonify(ageInMonths) 