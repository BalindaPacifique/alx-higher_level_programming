#!/usr/bin/python3
#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_add = 0
    for numbers_args in range(len(sys.argv) - 1):
        sum_add = sum_add + int(sys.argv[numbers_args + 1])
        print("{}".format(sum_add))
