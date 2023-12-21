import csv
import math


def task(csv_str: str):
    reader = csv.reader(csv_string.splitlines(), delimiter=',')
    data = list(reader)
    count = len(data)
    entropy_sum = 0

    for row in data:
        for cell in row:
            cell_value = cell
            if cell_value != '0':
                digit_value = float(cell_value) / (count - 1)
                entropy_sum += -digit_value * math.log2(digit_value)

    return round(entropy_sum, 1)


if __name__ == '__main__':
    csv_string = '1,0,4,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,2,1\n0,1,0,2,1\n'
    csv_string2 = '1,0,2,0,0\n2,1,2,0,0\n2,1,0,1,1\n0,1,0,1,1\n0,1,0,1,1\n0,1,0,1,1\n'
    entropy = task(csv_string)
    print(entropy)