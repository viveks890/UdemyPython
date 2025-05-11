import typing
import json

def read_json(path: str, mode: str = 'r') -> typing.Dict:
    file = open(path, mode)
    file_contents = json.load(file) # reads json data from file and converts it into python dictionary
    file.close()
    return file_contents

def export_json(file_contents, path: str, mode: str = 'w') -> None:
    file = open(path, mode)
    json.dump(file_contents, file)
    file.close()


fri = read_json('./friends_json.txt')

expt = export_json(fri,'./export_json.txt')