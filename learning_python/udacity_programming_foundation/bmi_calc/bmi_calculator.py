import time

message_txt = [
    "Welcome to the BMI Calculator\nPlease let me know your height in meters: ",
    "Now tell me how much you weight in KG: "
]
answers = []

for i in range(0, len(message_txt)):
    print(message_txt[i])
    answers.append(float(input()))
    time.sleep(1)

print("\nHold a second while I calculate your BMI ...")
bmi = str(round(answers[1] / (answers[0]**2), 2))
time.sleep(2)

print("Almost done...\n")
time.sleep(1)
print("Ok, done your BMI is " + bmi)
