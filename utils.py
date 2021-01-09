
def exist(json_data, key):
    return True if key in json_data.keys() else False

def query_to_mydict(dict):
    res = {}
    for key in dict:
        res[key] = dict[key]
    return res