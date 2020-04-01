# Variables, Lists, Sets, Tuples and Dictionaries

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
