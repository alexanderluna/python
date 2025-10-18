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

u = User('Alexander')
print(User.count)

"""
The output is 0 because Python will translate
self.count += 1 to self.count = self.count + 1 and call the build in
getattr(self, count) to get the count attribute followed by a call to
setattr(self, count, 1) which creates a new entry in __dict__ effectively
shadowing count.
"""