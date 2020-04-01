# Exception handling

When writting code its important to not just catch errors but also decide what
to do once an error occures.

```python
try:
  get_api_data()
except FailedApiFetching:
  print('Could not fetch data from API')
except Exception as err:
  print(str(err))
```

The idea is to fail gracefully. We can declare our own exception by creating an
empty class which inherits from the Exception class.

```python
class FailedApiFetching(Exception):
  pass
```

Although our class looks emtpy we are actually inheriting all the Exception
functionality from the Exception class which means our custom exception will
behave like any of python's built in exceptions.
