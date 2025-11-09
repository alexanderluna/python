# Algorithms

## [bitwise_compression.py](./bitwise_compression.py)

> open bitwise_compression.py in split mode

Compression algorithms provide a way to reduce memory size substantially at the
cost of speed. The easiest way to compress something is by picking the right
data type. Assuming you are storing a number and it defaults to
`signed long long int` (64-bit) in C but you know that your numbers are positive
and are never going to exceed 4294967295, then you can use an
`unsigned long int` (32-bit) or perhaps an even smaller `unsigned int` (16-bit).
Just with this small change you can save 50%-75% of memory.

Often times, you can convert types to improve efficiency. For example, strings
are lists of characters. If you know that you only need a small subset of the
characters or a combination of characters (currency ISO codes,
country ISO codes, nucleotides, etc.) you can assign an int to each character
and store them more effectually that way. While Python doesn't have 16-bit
integers, due to Python's object overhead, you can still use bitwise operations
to chain together bits in an integer.

```python
iso_germany: str = "DEU" # 0b01
iso_france: str = "FRA" # 0b11
bit_string: int = 1 # 0000 0001 - start with a sentinel

bit_string <<= 2 # 0000 0100 - push bits to the left by two places
bit_string |= 0b01 # 0000 0101 - bitwise-or adds 2 bits (01) to the end

bit_string <<= 2 # 0001 0100 - push bits to the left by two places
bit_string |= 0b11 # 0001 0111 - bitwise-or adds 2 bits (11) to the end

# 0001 0111
# 0000 0011 & = 0000 0011
bit_string >> 0 & 0b11
```

## [fibonacci.py](./fibonacci.py)

> open fibonacci.py in split mode

Fibonacci is a sequence of numbers where each number is the sum of the previous
two numbers except the first and second number.

0, 1, 1, 2, 3, 5, 8, 13...

fib(n) = fib(n - 1) + fib(n - 2)

Given that the algorithm to calculate a Fibonacci number involves calling the
same function but with n-1 and n-2 arguments, the simplest solution would be a
recursive function. While this approach works, every call to
`recursive_fibonacci()` will result in two more functions calls with n-1 and n-2
arguments growing exponentially. Also, the function does a lot of repetitive
calculation if you take a look at the call tree:

```python
fib 5 = fib 4 + fib 3
fib 4 = fib 3 + fib 2
fib 3 = fib 2 + fib 1
fib 3 = fib 2 + fib 1
fib 2 = fib 1 + fib 0
fib 2 = fib 1 + fib 0
fib 2 = fib 1 + fib 0
fib 1 = 1
fib 1 = 1
fib 1 = 1
fib 1 = 1
fib 0 = 0
fib 0 = 0
fib 0 = 0
```

This is a mayor performance bottleneck. That is where `memoization` comes in
handy. Memoization is a technique that can be used to store computational
heavy tasks or repetitive tasks. That way you can calculate each Fibonacci just
once, store it and retrieve the result rather than calculate it again. You can
use a `Dictionary` since it has fast write and read speeds or Python's build in
memoization decorator
[lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)

```python
calculated_fibs = {0: 0, 1: 1}

if n not in calculated_fibs:
    # do your thing
```

The recursive approach is nice and simple but it has one drawback. It can't
calculate the fibonacci for large numbers like 1028 because Python has a
built-in `RecursionError` when the recursion exceeds a limit.

It turns out, an even faster algorithm is to calculate the Fibonacci number
from the bottom up. You start at 0 and 1 and keep adding the last and next
number until you reach the desired Fibonacci.

```python
fib 1 = 0 + 1
fib 2 = 1 + 1
fib 3 = 1 + 2
fib 4 = 2 + 3
fib 5 = 3 + 5
```
