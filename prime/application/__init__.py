from flask import Flask, jsonify, Response 
import sys

app = Flask(__name__)

@app.route('/date/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):
     
    ageInMonths = int(ageInMonths)
    if ageInMonths > 1:
        if ageInMonths % 2 == 1 or ageInMonths == 2:
            prime = "yes, you are PRIME"
        elif ageInMonths % 2 != 1:
            prime = "No, you are COMPOSITE"
        else:
            prime = "You do not appear to exist"
    else:
        prime = "You do not appear to exist"
    print(str(prime), file=sys.stderr)
    print(str(prime), file=sys.stdout)
    return Response(str(prime))