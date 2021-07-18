import urllib.request
import json
import os

def read_json(file_path):
    open_file = open(file_path, 'r')
    data = json.load(open_file)
    converted = json.dumps(data, indent = 3)
    open_file.close()

    return(converted)


def read_all_json_files(file_path):
    for x in os.walk(file_path):
        file_list = []
        for y in x:
            if y.endswith('.json'):
                data = read_json(os.path.join(file_path, each))
                file_list.append(data)
    return file_list


def write_pickle(file_path, data):
    open_file = open(file_path, 'w')
    pickle.dump(data, open_file)


def load_pickle(file_path):
    open_file = open(file_path, 'r')
    data = pickle.load(open_file)
    return data
    
