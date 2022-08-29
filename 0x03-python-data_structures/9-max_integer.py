#!/usr/bin/python3
def max_integer(my_list=[]):
    """Function finds the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    bI = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > bI:
            bI = my_list[i]

    return (bI)
