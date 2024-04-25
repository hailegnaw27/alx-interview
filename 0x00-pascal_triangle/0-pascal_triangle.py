#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
"""
    Generates a list of lists representing Pascal's triangle up to n rows.
    
    Args:
        n (int): The number of rows to generate in the triangle.
    
    Returns:
        list: A list of lists representing the rows of Pascal's triangle
"""
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
