"""
In Python you can do two operations with a variable:

1. mutate -> names.append('john')
2. rebind -> names = ['john']

When you mutate, the variable scope doesn't matter.
When you rebind, only locally scoped variables can be used.

With this in mind, guess the output of the following piece of code.
"""

from functools import wraps


def metrics(fn):
    ncalls = 0
    name = fn.__name__

    @wraps(fn)
    def wrapper(*args, **kwargs):
        ncalls += 1
        print(f"{name} called {ncalls} times")

    return wrapper


@metrics
def increment(n):
    return n + 1


increment(5)

"""
This will raise an UnboundLocalError: cannot access local variable 'ncalls'
where it is not associated with a value

When Python sees the name 'ncalls', it looks for it in LEGB order:

Local
Enclosing (closure)
Global
Builtin

Integers are immutable in Python so Python tries to rebind the variable.
However, when you rebind, only locally scoped variables can be used.
If you want to rebind a global variable, you can use the nonlocal keyword
"""

from functools import wraps


def metrics(fn):
    ncalls = 0
    name = fn.__name__

    @wraps(fn)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        print(f"{name} called {ncalls} times")

    return wrapper


@metrics
def increment(n):
    return n + 1


increment(5)
