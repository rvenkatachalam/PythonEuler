"""Project Euler Problem 1
Find the sum of all the multiples of 3 or 5 below 1000.

This version uses a mathematical formula instead of iterating through every
number, which reduces the runtime to constant time.
"""


def sum_divisible_by(n, limit):
    """Return the sum of all multiples of ``n`` below ``limit``."""
    p = (limit - 1) // n
    return n * p * (p + 1) // 2


def solve(limit=1000):
    return (
        sum_divisible_by(3, limit)
        + sum_divisible_by(5, limit)
        - sum_divisible_by(15, limit)
    )


if __name__ == "__main__":
    print(solve())
