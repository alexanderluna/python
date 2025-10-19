"""
Most Python objects store their attributes in a dictionary and will try to
lookup the attribute in the following order:

1. __dict__     object
2. __class__    instance
3. __mro__      inheritance hierarchy
4. raise AttributeError

With this in mind, guess the output of the following piece of code.
"""


class User:
    count = 0

    def __init__(self, name):
        self.name = name
        self.count += 1


u = User("Alexander")
print(User.count)

"""
The output is 0 because Python will translate

self.count += 1 to self.count = self.count + 1 and call the build in
getattr(self, count) to get the count attribute followed by a call to
setattr(self, count, 1) which creates a new entry in __dict__ effectively
shadowing count.

Here is how the get_attr implementation looks like:
"""


def get_attr(obj, name):
    if name in obj.__dict__:
        print(f"found {name} in obj")
        return obj.__dict__[name]

    if name in obj.__class__.__dict__:
        print(f"found {name} in class")
        return obj.__class__.__dict__[name]

    for cls in obj.__class__.__mro__:
        if name in cls.__dict__:
            print(f"found {name} in {cls.__name__}")
            return cls.__dict__[name]

    raise AttributeError(name)
