#!/usr/bin/python3
"""
Pascal's Triangle Module

This module contains the function `pascal_triangle` that generates Pascal's
Triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists of int: Pascal's Triangle with n rows.
        Each row is represented as a list of integers.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [triangle[i - 1][j - 1] + triangle[i - 1][j]
                     for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
