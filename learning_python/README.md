# Learning

- [Learning](#learning)
  - [Introduction](#introduction)
  - [Data Structures](#data-structures)
  - [Indentation](#indentation)
  - [Variables, Lists, Sets, Tuples and Dictionaries](#variables-lists-sets-tuples-and-dictionaries)
  - [More on organizing Data](#more-on-organizing-data)

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

Using the **for/in** and **fot/not in** syntac we can loop lists. We can use
`.append`, `.remove`, `.pop`, `.extend` and `.insert` to mutate our list.

> When assigning a list to a new variable it DOES NOT create a copy of the list
> but assigns the reference to the same object. In order to copy, we can use
> the `.copy` method.

```python
vowels[start:stop:step]
```

Using this syntax we can access a portion of the array or a slice. Slicing a
list is non destructive unlike the method calls previous covered.

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
- `.interception`: compares two sets anda returns only the common items
