#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_leng = len(sys.argv)
    if arg_leng == 1:
        print("{} arguments.".format(arg_leng - 1))
    elif arg_leng == 2:
        print("{} argument:".format(arg_leng - 1))
    else:
        print("{} arguments:".format(arg_leng - 1))
    for number_args in range(1, arg_leng):
        print("{}: {}".format(number_args, sys.argv[number_args]))
