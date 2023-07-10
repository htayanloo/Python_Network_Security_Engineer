# save this as app.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/black")
def hello():
    data = {"blacklist":[{"ip":"1.1.1.1"}]}
    return jsonify(data)