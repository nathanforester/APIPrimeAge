from flask import Flask, jsonify, Response 
import sys

from datetime import datetime

app = Flask(__name__)

@app.route('/date/<birthDates>', methods=['GET', 'POST'])
def birthDate(birthDates):
    birthDates = int(birthDates)  
    year = datetime.utcnow().year
    ageInMonths = (int(year) - int(birthDates)) * 12
    print(str(ageInMonths), file=sys.stderr)
    print(str(ageInMonths), file=sys.stdout)
    return Response(str(ageInMonths))