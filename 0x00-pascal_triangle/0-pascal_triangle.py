#!/usr/bin/python3
"""
Graham S. Paul (0-pascal_triangle.py) - Restore a list of lists of
integers Constituting the Pascal’s triangle of n
"""


def pascal_triangle(n: int):
    """Restore an empty list if n <= 0"""

    if n <= 0:
        return []

    _list = []
    for i in range(n):
        row = [1]
        if _list:
            last_row = _list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        _list.append(row)
    return (_list)


if __name__ == "__main__":
    """test example"""
    def print_triangle(triangle):
        """Pulls a triangle"""
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
