#!/usr/bin/python3
def sum_arg(argv):
    i = len(argv) - 1
    if i == 0:
        print("{:d}".format(i))
        return
    else:
        numbers_args = 1
        sum_args = 0
        while numbers_args <= i:
            sum_args += int(argv[numbers_args])
            numbers_args = numbers_args + 1
        print("{:d}".format(sum_args))

if __name__ == "__main__":
    import sys
    sum_arg(sys.argv)
