#!/usr/bin/env python3
# กฤตเมธ ไทยเจริญ (กีตาร์)
# 630510609
# Lab11_2 
# 229223 Sec 002

import sys


def main():
    treasures = read_input()

    assert total_value('Gold', treasures) == 1090
    assert total_value('Ruby', treasures) == -1
    print("All OK!!!!")


def read_input():
    treasures = {}
    matrix = []
    # read file input
    for line in sys.stdin:
        if '#' in line:
            continue
        line = line.strip()
        matrix = line.split(',')
        # split text to list
        matrix = list(map(lambda x : x.strip(), matrix))
        matrix[2] = int(matrix[2])
        # add each element in to treasures
        if matrix[1] in treasures:
            treasures[matrix[1]] += [(matrix[0], matrix[2])]
        else:
            treasures[matrix[1]] = [(matrix[0], matrix[2])]

    return treasures


def total_value(treasure_type, treasures):
    total = 0
    # get key like a treasures_type
    val = (treasures.get(treasure_type, 0))

    #set return value
    if val == 0:
        total = -1
    else:
        for elememt in val:
            total += elememt[1]
    return total


if __name__ == '__main__':
    main()
