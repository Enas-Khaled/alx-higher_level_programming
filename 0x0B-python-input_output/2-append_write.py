#!/usr/bin/python3
""" Write in txt file """


def write_file(filename="", text=""):
    """append txt"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
