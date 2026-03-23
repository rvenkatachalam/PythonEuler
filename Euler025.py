# coding=utf-8
"""
Project Euler Problem 25
------------------------
Find the index of the first term in the Fibonacci sequence
to contain 1000 digits.

Fast approach used here:
- Instead of generating Fibonacci numbers one-by-one,
  we compute the answer directly with logarithms.
- This is effectively O(1) time.
"""

from math import ceil, log10, sqrt
from time import perf_counter


def first_fib_index_with_digits(digits):
    """
    Return the index n of the first Fibonacci number F(n)
    that has at least `digits` decimal digits.

    Why this works:
    ----------------
    1) Binet approximation for Fibonacci numbers:
           F(n) ≈ phi^n / sqrt(5)
       where phi = (1 + sqrt(5)) / 2

    2) A number has `digits` digits iff it is >= 10^(digits-1).
       So we need:
           phi^n / sqrt(5) >= 10^(digits-1)

    3) Taking log10 both sides gives:
           n * log10(phi) - log10(sqrt(5)) >= digits - 1

    4) Solve for n and round up to get the first valid index:
           n = ceil((digits - 1 + log10(sqrt(5))) / log10(phi))

    This avoids large integer arithmetic and repeated string conversion.
    """
    # Edge case: F1 = 1 is already 1 digit.
    if digits <= 1:
        return 1

    # Golden ratio.
    phi = (1 + sqrt(5)) / 2

    # Closed-form index computation.
    return int(ceil((digits - 1 + log10(sqrt(5))) / log10(phi)))


def main():
    """Compute and print the Project Euler 25 result with timing."""
    start = perf_counter()

    target_digits = 1000
    index = first_fib_index_with_digits(target_digits)

    elapsed_ms = (perf_counter() - start) * 1000.0

    print(index)
    print("Solution took: {:.3f} ms".format(elapsed_ms))


if __name__ == "__main__":
    main()
