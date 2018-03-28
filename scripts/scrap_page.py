from bs4 import BeautifulSoup
import requests

r = requests.get('https://mycroft1891.github.io')
soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
