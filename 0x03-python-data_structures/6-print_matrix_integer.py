#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for list in matrix:
        for element in list:
            print("{:d}".format(element), end="")
            if list.index(element) != len(list) - 1:
                print(" ", end="")
        print()
