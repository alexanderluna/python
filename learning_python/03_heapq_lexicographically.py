"""
Python has a build module, heapq, which implements a min-heap (binary tree)
where the parent node is always <= to its child notes. Pushing and deleting from
the heap are log(N) operations.

Heapq uses the comparison defined in the object type.

With this in mind, guess the output of the following piece of code.
"""

from heapq import heappush, heappop

tasks = []
heappush(tasks, (30, 'read a book'))
heappush(tasks, (10, 'drink coffee'))
heappush(tasks, (20, 0xCAFFE))
heappush(tasks, (20, 'take a walk'))
heappush(tasks, (40, 'go to bed'))

while tasks:
    _, payload = heappop(tasks)
    print(payload)

"""
This outputs TypeError: '<' not supported between instances of 'str' and 'int'

Our tasks heap objects are tuples which python sorts in a lexicographical order.
This means it compares the first 2 items, then the second 2 items and so on.
Our heap is looking something like this:

[
    (10, 'drink coffee'),   <- first to be popped
    (20, 'take a walk'),
    (20, 0xCAFFE),
    (30, 'read a book'),
    (40, 'go to bed')
]

When it reaches (20, 'take a walk') and (20, 0xCAFFE) it will compared them and
see that 20 and 20 are equal so it compares the str 'take a walk' to the
hexadecimal 0xCAFFE which is an int raising the exception.
"""