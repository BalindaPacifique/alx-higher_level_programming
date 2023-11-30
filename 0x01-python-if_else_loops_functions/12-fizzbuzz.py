#!/usr/bin/python3
def fizzbuzz():
    for indx in range(1, 101):
        if indx % 3 == 0 and indx % 5 == 0:
            print("FizzBuzz ", end="")
        elif indx % 3 == 0:
            print("Fizz ", end="")
        elif indx % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(indx), end="")
