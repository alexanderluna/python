# Threading

In python we can work with concurrent code thanks to the Threading module.

```python
from threading import Thread
```

To create a thread we create a Thread object. The object takes a target which is
the function to execute and args which are the arguments to pass to the
function.

```python
td = Thread(target=runMe, args=(time, job))
```

The result is a Thread object with our Thread which can be executed.

```python
td.start()
```