"""
In Python 3 the default encoding is UTF-8 which allows you to use Unicode
identifiers although it isn't recommended to use it this way.

tip: you get the π symbol on Mac by holding option + p.

With this in mind, guess the output of the following piece of code.
"""

π = 355 / 113
print(π)

"""
The output is indeed 3.14159292.... although we did integer division Python3
behaves less like C and returns a float. You can force Python 3 to return an
integer as well using the // operator 355 // 113
"""