#!/usr/bin/python3
for numbs in range(0, 90):
    if numbs % 10 > numbs / 10:
        if numbs != 89:
            print("{:02d}, ".format(numbs), end='')
        else:
            print("{:02d}".format(numbs))
