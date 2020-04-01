import time
import webbrowser

total_time = 60 * 60 * 2

for i in range(1,3):
    time.sleep(total_time)
    webbrowser.open("https://www.google.com")

# open google every 2 hours 3 times
