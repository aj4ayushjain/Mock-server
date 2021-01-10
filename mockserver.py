from flask import Flask, jsonify, request   
import json
from utils import query_to_mydict, key_exist, add_to_json, sort_json, delete_json, put_to_json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hellow_world():
    return "Hello WOrld"

@app.route("/<parent_identifier>", methods=['GET'])
def hello(parent_identifier):
    with open("store.json") as infile:
        data = json.load(infile)
    
    args =  request.args
    lst = data[parent_identifier]
    query_len = len(args)
    print(len(args))
    if not bool(args):
        return str(lst)

    else:
        newlist = []    
        mydict = query_to_mydict(args)
        
        if '_sort' in mydict.keys():
            return sort_json(parent_identifier, mydict)
        else:
            for row in lst:
                param_matched=0
                for key in mydict.keys():
                    print(key)
                    if key in row.keys() and mydict[key] == str(row[key]):
                        param_matched += 1
                    if param_matched == query_len:
                        newlist.append(row)
            return str(newlist)

@app.route("/<parent_id>/<int:id>/", methods=['GET'])
def fetch_id(parent_id, id):
    with open("store.json") as infile:
        data = json.load(infile)
    return data[parent_id][id]

@app.route("/<parent_identifier>", methods=['POST'])
def post(parent_identifier):
    
    data =  request.json

    return add_to_json(data, parent_identifier)

@app.route("/<parent_identifier>/<int:id>", methods=['PUT', 'PATCH'])
def put(parent_identifier, id):
    
    data =  request.json

    if 'id' in data:
        return "ID is Immutable"
    else:
        return put_to_json(id, data, parent_identifier)

@app.route("/<parent_identifier>/<int:id>", methods=['DELETE'])
def delete(parent_identifier, id):

    return delete_json(id, parent_identifier)

if __name__ == "__main__":
    app.run(host='0.0.0.0')