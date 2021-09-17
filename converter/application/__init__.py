from flask import Flask, jsonify, Response 

from datetime import datetime

app = Flask(__name__)

@app.route('/birthDate/<birthDate>', methods=['GET', 'POST'])
def birthDate(birthDate):
    birthday = birthDate 
    year = datetime.utcnow().year
    ageInMonths = (int(year) - int(birthday)) * 12
    return str(ageInMonths)