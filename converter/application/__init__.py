from flask import Flask, jsonify, Response 

from datetime import datetime

app = Flask(__name__)

@app.route('/birthDate/<int:birthdate>', methods=['GET', 'POST'])
def birthDate(birthdate):
    birthday = birthDate 
    year = datetime.utcnow().year
    ageInMonths = (int(year) - birthday) * 12
    return Response(ageInMonths)