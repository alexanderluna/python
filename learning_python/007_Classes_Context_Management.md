# Classes

Classes encapsulate state and behaviour. To create a class we use the class
keyword.

```python
class Home:
  pass
```

To create an object we just call the class like a function.

```python
my_home = Home()
your_home = Home()
```

While these 2 objects share behahior, they do not share state. Each object
manages its own state. When defining methods in python, the first argument
is a reference to the class itself.

```python
Home:
  def turn_on_the_lights(self):
    self.lights_on = true
```

> **self** is the equivalent of the **this** keyword in other programming
> languages

When creating an object, the init function of the class is called allowing us
to initialize attributes

```python
Home:
  def __init__(self, size: int, color: str):
    self.size = size
    self.color = color
```

classes are what allow us to hook into the context management protocol.

## Context Management Protocol

In python to work with the **with** statement we need our class to conform to
the **context management protocol**. This means that our class must define
2 magic methods:

- `__enter__`: setup everything before the with statement
- `__exit__`: clean up after the with statement

Using the database code from earlier, we want to setup the conection and cursor
in the enter method and we want to commit and close both the cursor and the
connection in the exit method.

```python
import mysql.connector

class MyDatabase:
  def __init__(self, config: dict)
    self.configuration = config

  def __enter__(self):
    self.connection = mysql.connector.connect(self.configuration)
    self.cursor = self.connection.cursor()
    return self.cursor

  def __exit__(self, execution_type, execution_value, execution_trace):
    self.connection.commit()
    self.cursor.close()
    self.connection.close()
```

Now that we are class conforming with the context management protocol we can use
it with the with statement.

```python
with MyDatabase(config_dictionary) as cursor:
  _sql = """some sql query"""
  cursor.execute(_sql, some_values)
```
