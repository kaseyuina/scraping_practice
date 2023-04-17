from bs4 import BeautifulSoup
import requests

# url = 'https://www.python.org/'
# url = 'https://tech-diary.net/python-scraping-books/'
url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'
target_url = url.format(1)
# r = requests.get(url)
r = requests.get(target_url)
soup = BeautifulSoup(r.text)
contents = soup.find_all('div', class_='cassetteitem')
# print(len(contents))
content = contents[0]
# print(content)
detail = content.find('div', class_='cassetteitem-detail')
table = content.find('table', class_='cassetteitem_other')
title = detail.find('div', class_='cassetteitem_content-title').text
address = detail.find('li', class_='cassetteitem_detail-col1').text
access = detail.find('li', class_='cassetteitem_detail-col2').text
age = detail.find('li', class_='cassetteitem_detail-col3').text

# print(title, address, access, age)

tr_tags = table.find_all('tr', class_='js-cassette_link')
tr_tag = tr_tags[0]
td_tag = [tag.text for tag in tr_tag.find_all('td')[2:6]]
print(td_tag)

# print(r.url)
# print(r.text)

# soup = BeautifulSoup(r.text)
# print(soup.find('h1').text)
# print(soup.find_all('h2')[0].text)

# h2_tag_list = []
# for i, h2_tag in enumerate(soup.find_all("h2")):
    # h2_tag_list.append(h2_tag.text)

# print(h2_tag_list)

# h2_tag_list2= [i.text for i in soup.find_all("h2")]
# print(h2_tag_list2)

# print(len(soup.find_all('span')))
# print(soup.find_all('span', class_=['say-no-more', 'message']))

# tag_list = [i.text for i in soup.find('article').find_all(['h2', 'h3'])]
# for i in tag_list:
    # print(i)

