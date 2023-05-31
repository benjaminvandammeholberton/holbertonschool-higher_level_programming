#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    res = a
    for i in range(1, abs(b)):
        res = res * a
        if b < 0:
            return (1 / res)
    return res
