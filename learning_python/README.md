# Learning

- [Learning](#learning)
  - [Introduction](#introduction)
  - [Data Structures](#data-structures)
  - [Indentation](#indentation)
  - [Variables, Lists, Sets, Tuples and Dictionaries](#variables-lists-sets-tuples-and-dictionaries)
  - [More on organizing Data](#more-on-organizing-data)
  - [Functions](#functions)
  - [Modules](#modules)
  - [Function quirks](#function-quirks)
  - [Web ApplicationsP](#web-applicationsp)

## Introduction

```python
from MODULE import FUNCTION
```

We can use this syntax to import a function from a module. A module a collection
of functions. The python language comes iwth the **standard library** which
provides a lot of resusable code. The standard lbirary is a collection of
modules each containing various functions. Some of the most common standard
library modules are:

- sys: system realted attributes
- os: interact with the operating system
- datetime: work with dates
- time: display and format time strings
- html: parse html escape and manipulate

## Data Structures

Python comes with built in data structures such as lists which are the
equivalent of arrays in other languages and can hold data of any type. Varibles
in Python are dynamically typed. They take the type from the object it is
assigned to. We can use **dot notation** to access nested attributes and
methods.

## Indentation

In python, every block of code (suite) is indented rather than delimitered with
parenthesis. A colon (:) introduces a new suite thus a new level of indentation
is required. Each suite can have neste suites each with a new level of
indentation.

## Variables, Lists, Sets, Tuples and Dictionaries

A variable takes the type of the value assigned to it. In python, everything is
an object thus all objects can be assigned to variables. Although everything is
an object, OOP is optional.

Python comes with 4 data structures to hold a collection of data:

- List: array like, indexed, mutable, heterogenous
- Tuple: array like, immutable, heterogenous
- Dictionary: hashtable, unordered, mutable, heterogenous
- Set: unordered, unique objects, mutable

```python
vowels = ['a', 'e', 'i', 'o', 'u']

for letter in vowel:
  print(letter)
```

Using the **for/in** and **for/not in** syntax we can loop lists. We can use
`.append`, `.remove`, `.pop`, `.extend` and `.insert` to mutate our list.

> When assigning a list to a new variable it DOES NOT create a copy of the list
> but assigns the reference to the same object. In order to copy, we can use
> the `.copy` method.

```python
vowels[start:stop:step]
```

Using this syntax we can access a portion of the array or a slice. Slicing a
list is non destructive unlike the method calls previously covered.

Dictionaries are a better option when we find ourselves keeping track of the
array's index to access data.

## More on organizing Data

Dictionaries are a powerful data structure optimized for reading and writing
data. To iterate over dictionaries, we can use the **for/in** loop. The loop
only loops over the keys but we can use those keys to access the associated
value. If we want to loop over both keys and values we can use the `.items`
method of the dictionary.

```python

fruits = { 'a': 'apple', 'b': 'banana' }

for key in fruits:
  print(key)

for key, value in fruits.items():
  print(key, value)
```

Similar we can use the **in** and **not in** operator to query a dictionary for
a key.

```python
'apple' in fruits
'orange' not in fruits
```

Sets on the other hand, have powerful methods that make certain operations
much faster such as which items overlap, are different and don't exist in
different sets. This behaves very similar like sets in mathematics.

- `.union`: combine to sets and return a unique set
- `.difference`: what is in one set but not in the other
- `.interception`: compares two sets and returns only the common items

## Functions

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

## Web ApplicationsP

Python comes with various modules that allow us to create web apps from scratch
but usually we do ourselves a favor by using pre-existing framework such as
Flask.

```bash
pip3 install flask
```

Flask is a micro framework. To use it, we can import it and create a simple
app.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() -> str
  return "Hello"

app.run()
```

When we run our web app we get a web server and a loopback address to access our
app in a browser. We have also seen our first decorator. A decorator allows us
to take existing code and augment its functionality without having to change
functions/classes.

If rendering simple text is too boring, we can use Jinja which a templating
engine that comes with Flask. Jinja allows us to dynamically render HTML.
