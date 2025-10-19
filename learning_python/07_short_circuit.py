"""
In Python 'and' and 'or' are short circuit operators.

With this in mind, guess the output of the following piece of code.
"""


def division(a, b):
    return a / b


if division(1, 2) > 0 or division(1, 0) > 0:
    print("OK")
else:
    print("ERROR")


"""
The output is OK

Dividing by 0 should raise a ZeroDivisionError. However, 'and' and 'or' are
short circuit operators which means the second argument will only be evaluated
if the first argument is false. This gives us an advantage when evaluating
potentially slow code.
"""

user = session.get("user") or load_user_from_db()

"""
load_user_from_db() is slower because it will query the database and return a
user. Thanks to the 'or' short circuit, session.get('user') will be evaluated
first and load_user_from_db() will not be evaluated unless there is not user in
the session.
"""
