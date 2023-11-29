#!/usr/bin/python3
for alphabet_low in range(97, 123):
    if alphabet_low == 101 or alphabet_low == 113:
        continue
    print("{}".format(chr(alphabet_low)), end='')
