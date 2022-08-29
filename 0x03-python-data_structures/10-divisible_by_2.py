#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiple = []

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            2multiple.append(True)
        else:
            2multiple.append(False)

    return (2multiple)
