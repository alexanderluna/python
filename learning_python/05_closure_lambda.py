"""
In Python, as in many other languages, you can define a function within a
function. The inner function grabs the objects defined in the enclosing scope
and associates them with the inner function object itself. This is a closure.

Python offers a way to declare anonymous functions with the lambda keyword.

With this in mind, guess the output of the following piece of code.
"""

display = []
buttons = []

for n in range(10):
    buttons.append(lambda: display.append(n))

print(n)
btn = buttons[5]
btn()
print(display)

"""
The output is [9]
range(10) goes from 1-9. At first it seems like each lambda should take in the
current value of n. However, each lambda uses the same n because by the time the
lambda is called the loop is finished and n = 9.

You can fix this behavior by creating a separate function
"""

display = []
buttons = []

def make_button(n):
    return lambda: display.append(n)

for n in range(10):
    buttons.append(make_button(n))

btn = buttons[5]
btn()
print(f'separate function: {display}')

"""
or passing n as a default function argument which works because default function
arguments are evaluated once at function creation which shadows the n from the
outer scope.
"""

display = []
buttons = []

for n in range(10):
    buttons.append(lambda n=n: display.append(n))

btn = buttons[5]
btn()
print(f'default argument: {display}')


