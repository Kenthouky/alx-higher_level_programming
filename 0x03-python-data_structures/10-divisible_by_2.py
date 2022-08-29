#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Function finds multiples of 2 in a list."""
    2multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            2multiples.append(True)
        else:
            2multiples.append(False)

    return (2multiples)
