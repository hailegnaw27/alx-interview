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
        list: A list of lists representing the rows of Pascal's triangle.
    """
    # Initialize an empty list to hold the rows of Pascal's triangle
    res = []
    
    # Check if n is greater than 0
    if n > 0:
        # Iterate through each row from 1 to n
        for i in range(1, n + 1):
            # Initialize a list to hold the current row
            level = []
            # Start with the binomial coefficient (C) set to 1
            C = 1
            # Iterate through each element in the current row
            for j in range(1, i + 1):
                # Append the current binomial coefficient to the row
                level.append(C)
                # Calculate the next binomial coefficient
                C = C * (i - j) // j
            # Append the current row to the list of rows
            res.append(level)
    
    # Return the list of rows representing Pascal's triangle
    return res

