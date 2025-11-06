# Algorithms

## [fibonacci.py](./fibonacci.py)

> open fibonacci.py in split mode

Fibonacci is a sequence of numbers where each number is the sum of the previous
two numbers except the first and second number.

0, 1, 1, 2, 3, 5, 8, 13...

fib(n) = fib(n - 1) + fib(n - 2)

Given that the algorithm to calculate a Fibonacci number involves calling the
same function but with n-1 and n-2 arguments, the simplest solution would be a
recursive function.

While this approach works, every call to `recursive_fibonacci()` will result in
two more functions calls with n-1 and n-2 arguments growing exponentially. Also,
the function does a lot of repetitive calculation if you take a look at the call
tree:

```sh
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
