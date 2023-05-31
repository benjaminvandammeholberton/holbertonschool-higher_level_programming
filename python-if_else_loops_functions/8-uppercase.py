#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 123 and ord(i) > 96:
            print(chr(ord(i) - 32), end="")
        else:
            print(i, end="")
