#!/usr/bin/python3
def uppercase(str):
    for iter in str:
        file = iter
        if ord(file) >= 97 and ord(file) < 123:
            file = chr(ord(iter) - 32)
            print(f"{file}", end="")
    print()
