#!/usr/bin/python3
""" Write in txt file """


def write_file(filename="", text=""):
    """Write in txt"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
