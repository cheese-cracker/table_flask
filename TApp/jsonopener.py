import json
import os
from TApp import appv

FIELDS = ['name', 'no_people', 'technology_tags', 'topic_tags']
FILE = "example"


def get_json_file(file_):
    file_name = os.path.join(appv.config['UPLOAD_FOLDER'], file_+'.json')
    # for root, dirs, files in os.walk("./TApp/upload_files"):
    #     for file in files:
    #         file_name = "./TApp/upload_files/" + str(file)
    with open(file_name, 'r') as working_file:
        jsonfl = json.load(working_file)
    return jsonfl


def get_flst():
    for root, dirs, files in os.walk(appv.config['UPLOAD_FOLDER']):
        file_list = [str(fil)[:-5] for fil in files]   # [:-5] to remove json
    return file_list
