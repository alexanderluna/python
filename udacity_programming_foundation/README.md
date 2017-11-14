# Udacity Programming Fundamentals with Python

[__VIEW COURSE ON UDACITY =>__](https://www.udacity.com/course/programming-foundations-with-python--ud036)


My repo for the programming fundamentals with Python Udacity course. Repo Index:

- [Installing Python](#install)
- [Taking a break](#take-brake)
- [Secret Message](#secret-message)
- [Draw Art](#draw-art)
- [Send Text](#send-text)
- [Challenge: Build program with a built in function](#challenge)


## <a name="install">Install Python</a>

Install homebrew:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install python 3:

```
brew install python3
```

If you have problems installing python3 in MacOS High Sierra read this [stackoverflow post](https://stackoverflow.com/questions/47255517/brew-install-python3-didnt-install-pip3)


## <a name="take-brake">Taking a break</a> [(View Source)](break_time.py)

Task: Remember every X amount of time the user to take a break and do something else.

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


## <a name="secret-message">Secret Message</a> [(View Source)](rename_files.py)

Task: Decrypt secret message by removing numbers from the file name.

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


## <a name="draw-art">Draw Art</a> [(View Source)](mindstorms.py)

Task: Draw a circle with a square

Planning the app

```
import libraries

create a square

loop x amount of times
  draw square
  turn by X degrees
```

import the required libraries to draw to a canvas:

```
import turtle
```

create square

```
def draw_square():
  for i in range(1,5):
    custom_turtle.forward(100)
    custom_turtle.right(90)
```

loop and offset by X amount of degrees on each loop:
```
for i in range(1,100):
  draw_square(alex)
  alex.right(5)
```


## <a name="send-text">Send Text</a> [(View Source)](send_text.py)

Task: Send an SMS to your phone

Planning the program outline:

```
import libraries

setup a connection to SMS service
setup message

send message
```

import the required libraries

```
import boto3
```

setup a connection to SMS service (AWS SNS)

```
client = boto3.client(
    "sns",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
    aws_secret_access_key=os.environ["AWS_SECRET_KEY"],
    region_name="us-east-1"
)
```

setup message and send message

```
client.publish(
    PhoneNumber=os.environ['MY_PHONE_NUMBER'],
    Message="Sending you a message with AWS"
)
```


## <a name="challenge">Build program with a built in function</a> [(View Source)](bmi_calculator.py)

Task: Build a program with a built in function

Plan the program layout of the BMI calculator:

```
import libraries

prompt user message
save input

perform calculation
print the result
```

Import the time library to control time during the execution:

```
import time
```

now prompt the user with messages:

```
for i in range(0, len(message_txt)):
    print(message_txt[i])
    answers.append(float(input()))
    time.sleep(1)
```

do some calculation and return the results

```
print("\nHold a second while I calculate your BMI ...")
bmi = str(round(answers[1] / (answers[0]**2), 2))
print("Ok, done your BMI is " + bmi)
```
