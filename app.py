
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world"

@app.route('/predict', methods = ['POST'])
def predict():
    cgpa = request.form.get('cgpa')
    iq = request.form.get('iq')
    profile_score = request.form.get('profile_score')
    result = "YES"

    return jsonify({'placement': result})


if __name__ == "__main__":
    app.run(debug = True)
