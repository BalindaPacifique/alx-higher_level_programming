#!/usr/bin/python3
"""Creates a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file to write."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
