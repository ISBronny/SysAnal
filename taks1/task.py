import csv
from typing import Tuple
import sys


def get_from_csv(file: str, address: Tuple[int, int]):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return list(reader)[address[0]][address[0] - 1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = len(sys.argv)

    print(get_from_csv('../data/test.csv', (2, 2)))
