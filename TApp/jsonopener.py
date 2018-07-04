import json
# import os

FIELDS = ['name', 'no_people', 'technology_tags', 'topic_tags']
FILE = "example"


def get_json_file(file_):
    file_name = './TApp/upload_files/'+file_+'.json'
    # for root, dirs, files in os.walk("./TApp/upload_files"):
    #     for file in files:
    #         file_name = "./TApp/upload_files/" + str(file)
    with open(file_name, 'r') as working_file:
        jsonfl = json.load(working_file)
    return jsonfl
