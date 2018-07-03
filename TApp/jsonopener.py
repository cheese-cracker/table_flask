import json


FIELDS = ['name', 'no_people', 'technology_tags', 'topic_tags']


def get_json_file():
    file_name = 'TApp/upload.json'
    with open(file_name, 'r') as working_file:
        jsonfl = json.load(working_file)
    return jsonfl
