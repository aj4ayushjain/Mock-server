from flask import Flask, jsonify, request   
import json
from utils import query_to_mydict, key_exist

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

def add_to_json(json_data, parent_identifier):
    response = {}
    print(json_data)
    
    with open('store.json', 'r') as data_file:
        data = json.load(data_file)
    
    if key_exist(data, parent_identifier):
        rows = data[parent_identifier]
        entity_id = json_data['id']
        existing_entity = list(filter(lambda x: (x['id'] == entity_id), rows))
        if len(existing_entity) == 0:
            data[parent_identifier].append(json_data)
            with open('store.json', 'w') as data_file:
                json.dump(data, data_file)
            response["message"] = "SuccessFully Added new Post"
        else:
            response["message"] = "Please Try with diffrent Key"
    else:
        data[entity] = []
        data[parent_identifier].append(json_data)
        with open('store.json', 'w') as data_file:
            json.dump(data, data_file)
        response["message"] = "SuccessFully Added new Post"
    return response

@app.route("/<parent_identifier>/<int:id>", methods=['PUT', 'PATCH'])
def put(parent_identifier, id):
    
    data =  request.json

    if 'id' in data:
        return "ID is Immutable"
    else:
        return put_to_json(id, data, parent_identifier)

def put_to_json(pk, json_data, parent_identifier):
    response = {}
    with open('store.json', 'r') as data_file:
        data = json.load(data_file)
    if key_exist(data, parent_identifier):
        is_updated = False
        if len(data[parent_identifier]):
            for row in data[parent_identifier]:
                if row['id'] == pk:
                    for key, value in json_data.items():
                        row[key] = value
                    is_updated = True
                    break
        if is_updated:
            response["message"] = "Successfully Updated Post Data"
            with open('store.json', 'w') as data_file:
                json.dump(data, data_file)
        else:
            response["message"] = "No Value for this id."
    else:
        response["message"] = "No Entity with this Name "+ parent_identifier
    return response

@app.route("/<parent_identifier>/<int:id>", methods=['DELETE'])
def delete(parent_identifier, id):

    return delete_json(id, parent_identifier)


def delete_json(pk, parent_identifier):
    response = {}
    with open('store.json', 'r') as data_file:
        data = json.load(data_file)

    if key_exist(data, parent_identifier):
        is_deleted = False
        if len(data[parent_identifier]):
            for row in data[parent_identifier]:
                if row['id'] == pk:
                    data[parent_identifier].remove(row)
                    is_deleted = True
                    break
        if is_deleted:
            response["message"] = "Successfully Deleted Data"
            with open('store.json', 'w') as data_file:
                json.dump(data, data_file)
        else:
            response["message"] = "No Elements for this id."
    else:
        response["message"] = "No Elements for this Entity"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')