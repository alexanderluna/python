import urllib.request
import urllib.parse

def read_text():
    my_file = open("/Users/alexander/Desktop/python/udacity_programming_foundation/movie_quotes.txt")
    quotes = my_file.read()
    my_file.close()
    print("Sending request\n")
    check_bad_words(quotes)

def check_bad_words(some_text):
    some_text = urllib.parse.quote_plus(some_text)
    request = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+ str(some_text))
    response = request.read().decode("UTF-8")
    if response == "true":
        print("Oh shit there is a bad word")
    elif response == "false":
        print("Welp, looks all fine")
    else:
        print("We fucked up")
    request.close()

read_text()
