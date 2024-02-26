#!/usr/bin/python3
# Graham S. Paul - 0-making_change.py
"""Creating a change"""


def makeChange(coins, total):
    """The classic Bottom-Up dynamic programming."""
    temp_value = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0

    for coin in coins:
        if total % coin <= total:
            temp_value += total // coin
            total = total % coin

    return temp_value if total == 0 else -1


if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))

    print(makeChange([1256, 54, 48, 16, 102], 1453))
