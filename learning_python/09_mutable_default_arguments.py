"""
As mentioned previously in 05_closure_lambda.py, default arguments are evaluated
once when the function is defined.

With this in mind, guess the output of the following piece of code.
"""

import re
from collections import defaultdict


def word_frequency(text, freqs=defaultdict(int)):
    for word in [w.lower() for w in re.findall(r"\w+", text)]:
        freqs[word] += 1
    return freqs


f1 = word_frequency("Hello world 👋")
f2 = word_frequency("Merry Christmas 🎄")

print(f1)
print(f2)

"""
This outputs:
defaultdict(<class 'int'>, {'hello': 1, 'world': 1, 'merry': 1, 'Christmas': 1})
defaultdict(<class 'int'>, {'hello': 1, 'world': 1, 'merry': 1, 'Christmas': 1})

The default argument 'defaultdict(int)' is evaluated once and since dict and
list are mutable this results in a mutable default argument or a permanent
object. You can fix this by setting the default to None 'freqs=None'.
"""
