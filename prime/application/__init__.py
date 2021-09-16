from flask import Flask, jsonify, Response 

app = Flask(__name__)

@app.route('/prime/<int:birthDate>', methods=['GET', 'POST'])
def prime(birthDate):
    if birthDate > 1:
        if birthDate % 2 == 1 or birthDate == 2:
            prime = "PRIME number"
        elif birthDate % 2 != 1:
            prime = "COMPOSITE number"
        else:
            prime = "You do not appear to exist"
    else:
        prime = "You do not appear to exist"
    return Response(jsonify(str(prime))) 