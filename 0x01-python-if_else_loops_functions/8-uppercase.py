#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
        else:
            c = chr(ord(str[i]))
        print("{0}".format(c), end="")
    print()
