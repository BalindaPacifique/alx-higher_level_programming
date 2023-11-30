#!/usr/bin/python3
def uppercase(str):
    for iter in str:
        if ord(iter) >= 97 and ord(iter) <= 122:
            iter = chr(ord(iter) - 32)
            print("{}".format(iter), end="")
    print()
