#!/usr/bin/python3
"""Creates a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file."""
    texts = ""
    with open(filename) as r:
        for line in r:
            texts += line
            if search_string in line:
                texts += new_string
    with open(filename, "w") as w:
        w.write(texts)
