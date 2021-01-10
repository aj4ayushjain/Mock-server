import json

"""
Utility Function to be used all over the app

"""
def key_exist(json_data, key):
    return True if key in json_data.keys() else False

def query_to_mydict(dict):
    res = {}
    for key in dict:
        res[key] = dict[key]
    return res

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

def sort_json(parent_identifier, mydict):

    response = {}
    with open('store.json') as json_file:
        data = json.load(json_file)

    if key_exist(data, parent_identifier):
        rows = data[parent_identifier]
        response[parent_identifier] = []
        if len(rows):
            sort_value = mydict['_sort']
            for row in rows:
                if sort_value in row.keys():
                    response[parent_identifier].append(row)
            if len(response[parent_identifier]):
                sort_order = mydict['_order']
                reverse = False if sort_order == 'asc' else True
                response[parent_identifier] = sorted(response[parent_identifier], key = lambda i: i[sort_value], reverse=reverse)
    else:
        response["message"] = "No Entity is present with Name " + parent_identifier
    return response

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
