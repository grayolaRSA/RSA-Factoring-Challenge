#!/usr/bin/python3
"""module obtains 2 factors of a number"""


import math
import sys


def get_factor(n):
    """function gets two factors by dividing
    first by lowest prime number
    then by result of using prime number as divisor"""

    if n < 2:
        return None
    if n == 2:
        return (1, 2)

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return (i, n // i)


def main():
    """function to open test file to run get_factor"""

    if len(sys.argv) < 2:
        print("Usage: python <file_name> <test_file>")
        return

    file_name = sys.argv[1]

    with open(file_name, 'r') as f:
        for line in f:
            n = int(line.strip())

            factors = get_factor(n)

            if factors:
                print("{:d}={:d}*{:d}".format(n, factors[0], factors[1]))
            else:
                print("{:d} must have two factors".format(n))


if __name__ == "__main__":
    main()
