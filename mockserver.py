from flask import Flask, jsonify
import json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def hellow_world():
    return "Hello WOrld"

@app.route("/<parent_identifier>/", methods=['GET'])
def hello(parent_identifier):
    with open("store.json") as infile:
        data = json.load(infile)
    return str(data[parent_identifier])

@app.route("/<parent_id>/<int:id>/", methods=['GET'])
def fetch_id(parent_id, id):
    with open("store.json") as infile:
        data = json.load(infile)
    return data[parent_id][id]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
