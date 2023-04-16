import requests
from bs4 import BeautifulSoup

# url = 'https://www.python.org/'
url = 'https://tech-diary.net/python-scraping-books/'
r = requests.get(url)

# print(r.url)
# print(r.text)

soup = BeautifulSoup(r.text)
print(soup.find('h1').text)