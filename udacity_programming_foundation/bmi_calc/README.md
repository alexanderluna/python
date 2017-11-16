# Build a program with a built-in function [(View Source)](bmi_calculator.py)

[<= GO BACK](../README.md)

__Task: Build a program with a built in function__

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
