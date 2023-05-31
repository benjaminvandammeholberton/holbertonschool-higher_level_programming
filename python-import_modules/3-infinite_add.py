#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 0:
        print(0)
    res = 0
    for i in range(1, len(sys.argv)):
        y = int(sys.argv[i])
        res = res + y
    print(res)
