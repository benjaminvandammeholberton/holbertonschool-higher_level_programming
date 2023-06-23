#!/usr/bin/python3
"""
Module containing the function pascal_triangle.
"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the given number of rows (n).

    Args:
        n (int): Number of rows to generate in Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle up to the given
        number of rows.
    """

    if n <= 0:
        return []

    pascal = [[]]
    m = 0

    for i in range(n):
        add1 = 0
        add2 = 0
        pascal[i].append(1)
        if i >= 2:
            for j in range(m):
                pascal[i].append(pascal[i - 1][add1] + pascal[i - 1][add2 + 1])
                add1 += 1
                add2 += 1
        if i != n - 1:
            pascal.append([])
        if i >= 1:
            pascal[i].append(1)
            m += 1
    return pascal
