"""
Fibonacci is a sequence of numbers where each number is the sum of the previous
two numbers except the first and second number.

0, 1, 1, 2, 3, 5, 8, 13...

fib(n) = fib(n - 1) + fib(n - 2)
"""

from functools import lru_cache
from typing import Generator


@lru_cache(maxsize=None)
def recursive_fibonacci(n: int) -> int:
    """
    use recursion to calculate each fibonacci
    use memoization to store the result of previously calculated fibonacci
    limited by maximum recursion depth
    """
    if n < 2:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def iterative_fibonacci(n: int) -> int:
    """
    iteratively calculate the fibonacci number
    """
    if n == 0:
        return 0

    last: int = 0
    next: int = 1

    for i in range(1, n):
        last, next = next, last + next  # tuple unpacking for simplicity

    return next


def generated_fibonacci(n: int) -> Generator[int, None, None]:
    """
    iteratively generate the fibonacci sequence up to a given number
    """
    yield 0

    if n > 0:
        yield 1

    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    print("Recursive Fib: ", recursive_fibonacci(50))
    print("Iterative Fib: ", iterative_fibonacci(50))

    for i in generated_fibonacci(50):
        print(i)
