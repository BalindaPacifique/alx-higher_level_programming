#!/usr/bin/python3
for two_dig_numbers in range(0, 100):
    if two_dig_numbers == 99:
        print("{}".format(two_dig_numbers))
    else:
        print("{:02d}, ".format(two_dig_numbers), end='')
