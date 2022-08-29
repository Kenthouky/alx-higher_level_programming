#!/usr/bin/python3
def no_c(my_string):
    """Remove all c and C from string."""
    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new_string))
