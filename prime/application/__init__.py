from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<birthday>')
def prime(birthday):
    if birthday > 1:
        if birthday % 2 == 1 or birthday == 2:
            prime = "PRIME number"
        elif birthday % 2 != 1:
            prime = "COMPOSITE number"
        else:
            prime = "You do not appear to exist"
    else:
        prime = "You do not appear to exist"
    return jsonify(prime) 