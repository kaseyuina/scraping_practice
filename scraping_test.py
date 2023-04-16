import requests
from bs4 import BeautifulSoup

url = 'https://www.python.org/'
# url = 'https://tech-diary.net/python-scraping-books/'
r = requests.get(url)

# print(r.url)
# print(r.text)

soup = BeautifulSoup(r.text)
# print(soup.find('h1').text)
# print(soup.find_all('h2')[0].text)
h2_tag_list = []
for i, h2_tag in enumerate(soup.find_all("h2")):
    h2_tag_list.append(h2_tag.text)

print(h2_tag_list)

h2_tag_list2= [i.text for i in soup.find_all("h2")]
print(h2_tag_list2)