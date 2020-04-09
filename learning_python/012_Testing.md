# Testing

Testing is the key to robust code. As projects grow, it becomes increasingly
important to make sure everything is working the way it should. We can get
started with testing in python by importing the **unittest** module.

```python
import unittest
```

Now can create a simple a function and a test that goes with.

```python
# add.py

def add(a: int, b: int) -> int:
  return a + b
```

We can create now a test for this function. First we import the unittest module
and the file.

```python
# test.py
import unittest
import add

class TestAdd(unittest.TestCase):
  def test_add(self):
    a = 10
    b = 15
    result = add.add(a, b)
    self.assertEqual(result, 25)

unittest.main()
```

To run our test we can just run it like a normal python program.

```bash
python3 test.py
```
