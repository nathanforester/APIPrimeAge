from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<dob>')
def prime(dob):
    if dob > 1:
        if dob % 2 == 1 or dob == 2:
            prime = "PRIME number"
        elif dob % 2 != 1:
            prime = "COMPOSITE number"
        else:
            prime = "You do not appear to exist"
    else:
        prime = "You do not appear to exist"
    return jsonify(prime) 