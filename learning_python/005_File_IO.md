# Read and Write to Files

Python comes with a built in support for open, process and close. We open a
file, process the data and close the file when we are done.

```python
my_file = open('myfile.txt', 'a') # open a new file
print('Hello there', file=my_file) # write some data
my_file.close() # save it
```

The first argument of open specifies the file we want to open. The second
argument specifies the **mode** we want to open the in.

| r    | w     | a      | x      |
| ---- | ----- | ------ | ------ |
| read | write | append | create |

> We can also combine the modes rw, ax

To read the content of a file we can open it and loop over the lines.

```python
myfile = open('myfile.txt')

for line in myfile:
  print(line)

myfile.close()
```

Thus far we used open, process and close to work with files. However, it is more
common to use the **with** statement to avoid having to close the line manually.

```python
with open('myfile.txt') as line:
  print(line)
```

> A final note on HTML in data files: make sure to escape HTML before you save
> it for safety reasons. In flask, we can use the **escape** function for that.
