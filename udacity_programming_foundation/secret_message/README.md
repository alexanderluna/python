# Secret Message [(View Source)](rename_files.py)

[<= GO BACK](../README.md)

__Task: Decrypt secret message by removing numbers from the file name.__

Planning the program outline:

```
import libraries

open current_directory

loop through current_directory
  rename each file in current_directory
```

Importing libraries needed to access the File system and rename files:

```
import os
```

open directory and list files in the opened directory:

```
path_name = r"/Users/alexander/Documents/developement/prank"
file_list = os.listdir(path_name)
os.chdir(path_name)
```

loop though the chosen directory:

```
for old_name in file_list:
```

remove numbers from the file name and rename the file:

```
new_name = old_name.translate(None, "0123456789")
print("Changing " + old_name + " to " + new_name)
os.rename(old_name, new_name)
```
