# Taking a break [(View Source)](break_time.py)

[<= GO BACK](../README.md)

__Task: Remember every X amount of time the user to take a break and do something else.__

Planning the program outline:

```
import time library

loop X amount of time:
  open Browser and navigate to URL
```

Importing libraries needed to open Web Browser and control time:

```
import webbrowser
import time
```

add the loop for X amount of times without creating an index:

```
for i in range(1,3):
```

Pause time and open browser on each loop:

```
time.sleep(total_time)
webbrowser.open("https://www.google.com")
```
