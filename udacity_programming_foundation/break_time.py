import time
import webbrowser

count = 0
total_breaks = 3
total_time = 60 * 60 * 2

while count < total_breaks:
    time.sleep(total_time)
    webbrowser.open("https://www.google.com")
    count = count + 1


# open google every 2 hours 3 times
