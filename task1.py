import csv
import json

from jsonpath_ng import jsonpath, parse
from typing import Tuple


class System:
    def __init__(self, name: str):
        self.name = name

    def send_message(self, message):
        print(f'{self.name}: {message}')


def get_from_csv(file: str, address: Tuple[int, int]):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return list(reader)[address[0]][address[0]-1]

def get_from_json(file: str, jpath: str):
    with open(file, 'r') as json_file:
        json_data = json.load(json_file)

    jsonpath_expression = parse(jpath)

    return jsonpath_expression.find(json_data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(get_from_csv('data/test.csv', (2, 2)))
    print(get_from_json('data/test.json', 'test.value1')[0].value)
