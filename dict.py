import json

# read json file as dict
def open_dict():
    with open('words_dictionary.json', 'r') as json_file:
        dict = json.load(json_file)
    return dict
