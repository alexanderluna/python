# Check for profanity [(View Source)](check_profanity.py)

[<= GO BACK](../README.md)

__Task: Scan text for profanity words and alert the user if there are any.__

Planning the program outline:

```
import libraries

open document
read read document

send document content via HTTP request
parse response

alert the user of outcome
```

Importing libraries needed to send HTTP requests:

```
import urllib.request
import urllib.parse
```

open document and read the content of it.

```
my_file = open("location/of/text.txt")
lines = my_file.read()
```

send text file content via HTTP and handle response. Send response to user with an if else statement:

```
request = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ str(some_text))
response = request.read().decode("UTF-8")
```
