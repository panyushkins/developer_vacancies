import json


def save_to_file(file_name, save_file):
    with open(file_name, 'w') as file:
        json.dump(save_file, file)


def read_from_file(file_path):
    with open(file_path, 'r') as file:
        json_file = json.load(file)
    return json_file
