"""
Python doesn't have private and protected attributes. It follows the convention
that attributes prefixed with a _ are considered an implementation detail.
However, nothing prevents you from accessing it even tho you shouldn't
access it because it can change in the next update.

With this in mind, guess the output of the following piece of code.
"""

next_uid = 1


class User:
    def __init__(self, name):
        global next_uid
        self.name = name
        self.__id = next_uid
        next_uid += 1


u = User("john")
print(f"name={u.name}, id={u.__id}")

"""
The output is an AttributeError: 'User' object has no attribute '__id'

When you use __id, it will block all subclasses of the User class from
using their own __id attribute. Therefore, Python provides something
called 'name mangling' (it is also used in C, Java and other languages).
"""

print(vars(u))  # {'name': 'john', '_User__id': 1}

"""
Within the User class you can access __id but from the outside, the
attribute is changed to _User__id freeing up names classes can use for
nonpublic attributes
"""
