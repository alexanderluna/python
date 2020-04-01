# Functions

```python
def greet_someone(name):
"""Greet someone by name"""
  return "Hello {}".format(name)

greet_someone()
```

> Strings can be written using single or double quote but the advice is to pick
> one and stick to it.

Python functions allow you to use docstrings to document your function as your
write them. Python 3 introduced a new concept called **annotation** which
allows us to hint what data type the function arguments expect and what it will
return.

> Annotations are optional and do not enforce type checking

```python
def greet_someone(name:str) -> str:
  return "Hello {}".format(name)
```

Annotations help programmers understanding code better. Furthermore, we can
assign default values to our function arguments as well.

```python
def greet_someone(name:str="Alexander") -> str:
```

Thus far our functions have accepted positional arguments which means the
position of the arguments matters. We can however use keyword arguments.

```python
def greet_someone(greeting="Hello", name="Alexander"):
```

## Modules

Multiple functions can be shared easily through modules. When importing a
function the interpreter looks at the current directory first followed by:

1. site-packages folder
2. standard library

For wider support of modules, we can add our modules to the site-packages folder
through `setuptools`.

1. create setup.py and README.md (import setuptools, configure the module)
2. `python3 setup.py sdist` (run the setup script which creates an archive)
3. `pip3 install my_module.tar.gz` (install the archive file)

> We can use this generated archive file to share it with others on PyPI.

## Function quirks

Python function arguments are neither passed **by-reference** nor **by-value**
always. Mutables objects such as Dictionaries, Lists and Sets are passed
**by-reference** and Immutable objects such as Strings, Integers and Tuples are
passed **by-value**.
