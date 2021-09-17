from flask import Flask, jsonify, Response 

app = Flask(__name__)

@app.route('/prime/<ageInMonths>', methods=['GET', 'POST'])
def prime(ageInMonths):

    if int(ageInMonths) > 1:
        if int(ageInMonths) % 2 == 1 or int(ageInMonths) == 2:
            prime = "PRIME number"
        elif int(ageInMonths) % 2 != 1:
            prime = "COMPOSITE number"
        else:
            prime = "You do not appear to exist"
    else:
        prime = "You do not appear to exist"
    
    return str(prime)