#!/usr/bin/python3:
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None

    for row in matrix:
        for i, element in enumerate(row):
            if i > 0:
                print(" ", end="")
            print("{:d}".format(element), end="")
        print()
