#!/usr/bin/python3
for alphabets in range(122, 96, -1):
    if alphabets % 2:
        alphabets = alphabets - 32
    print("{:c}".format(alphabets), end="")
