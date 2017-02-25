import json


def save_to_file(file_name, save_file):
    with open(file_name, 'w') as file:
        json.dump(save_file, file)