"""
Python has several hooks to speed up the attribute lookup algorithm:

1. __getattr__
2. __getattribute__
3. staticmethod
4. classmethod

__getattr__ is called when the regular lookup fails but __getattribute__
bypasses the attribute lookup.

With this in mind, guess the output of the following piece of code.
"""


class Seeker:
    def __getattribute__(self, name):
        if name not in self.__dict__:
            return "<not found>"
        return self.__dict__[name]


s = Seeker()
print(s.id)

"""
The output is a RecursionError: maximum recursion depth exceeded

Since __getattribute__ bypasses the lookup, self.__dict__ will call
__getattribute__ on itself again.

The good news is, that once the Python call stack size is greater than the
sys.getrecursionlimit() a RecursionError will be raised protecting our code from
an infinite recursion.

You can implement hooks for your dictionaries as well using the
collection.defaultdict and __missing__.
"""
