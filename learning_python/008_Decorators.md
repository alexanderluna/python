# Decorators

A decorator allows us to ammend a function without changing the function. To
understand decorators we need to cover some ground first. A function take another function as an argument specifically we pass a function object.

```python
def apply(function: object, value: object) -> object:
  return function(value)
```

A function can contain another function

```python
def hello():
  def goodbye():
    print(' and goodbye')
  print('hello')
  goodbye()
```

Finally, a function can accept a varying list of arguments

```python
def my_function(*args):
  for arg in args:
    print(arg)

args = [1,2,'hello','bye']

my_function(args) # [1,2,'hello','bye']
my_function(*args) # 1,2,'hello','bye'
```

It is also possible to accept arbitrary keyword arguments.

```python
def my_function(**kwargs):
  for key, value in kwargs.items():
    print(key, value)
```

Now we can define a decorator. A decorator is a function that takes the
decorated function as an argument and returns a new function with the same
signature as the decorated function.

```python
def check_logged_in(func):
  def wrapper(*args, **kwargs):
    if 'logged_in' in session:
      return func(*args, **kwargs)
    return 'not logged in'
  return wrapper
```

This works because a function identifies itself but it is possible for a
function to forget its identity which is why we can use a module to handle the
details.

```python
from functools import wraps

def check_logged_in(func):
  @wrap(func)
  def wrapper(*args, **kwargs):
  # ...
```
