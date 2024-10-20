# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt

# csv data contains details of club names, city and country they belong to
# need to convert it into a json having keys and club, city, country

import json
import typing
import pprint


def load_csv(path: str, mode: str='r') -> typing.List:
    with open(path, mode) as file_pointer:
        file = file_pointer.readlines()
    return file

def prepare_data(file: typing.List) -> typing.List:
    file = [file.strip() for file in file]
    my_list = []
    for detail in file:
        my_dict = dict()
        detail = detail.split(',')
        my_dict['club'] = detail[0]
        my_dict['city'] = detail[1]
        my_dict['country'] = detail[2]
        my_list.append(my_dict)
    return my_list

def load_json(my_list: typing.List, json_file_path: str, mode:str = 'w') -> None:
    # json_obj = json.dump(my_json)
    with open(json_file_path, mode) as json_file:
        json.dump(my_list,json_file,indent=4)
    return None

my_data = load_csv('./csv_file.txt')

data_list = prepare_data(my_data)

load_json(data_list, './json_file.txt')

pprint.pprint(json)