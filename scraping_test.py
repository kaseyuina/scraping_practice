from time import sleep
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint

# url = 'https://www.python.org/'
# url = 'https://tech-diary.net/python-scraping-books/'
url = 'https://suumo.jp/chintai/tokyo/sc_shinjuku/?page={}'
d_list = []

for i in range(1, 3):
    print('d_listの大きさ：', len(d_list))
    target_url = url.format(i)
    
# target_url = url.format(1)
# r = requests.get(url)
    r = requests.get(target_url)
    soup = BeautifulSoup(r.text)

    sleep(1)
    contents = soup.find_all('div', class_='cassetteitem')
    # print(len(contents))
    # content = contents[0]
    # print(content)
    for content in contents:
        detail = content.find('div', class_='cassetteitem-detail')
        table = content.find('table', class_='cassetteitem_other')
        title = detail.find('div', class_='cassetteitem_content-title').text
        address = detail.find('li', class_='cassetteitem_detail-col1').text
        access = detail.find('li', class_='cassetteitem_detail-col2').text
        age = detail.find('li', class_='cassetteitem_detail-col3').text

        # print(title, address, access, age)

        tr_tags = table.find_all('tr', class_='js-cassette_link')
        for tr_tag in tr_tags:
            floor, price, first_fee, capacity = tr_tag.find_all('td')[2:6]
            fee, management_fee = price.find_all('li')
            deposite, gratuity = first_fee.find_all('li')
            madori, menseki = capacity.find_all('li')
            # print(td_tag)
            d = {
                'title': title,
                'address': address,
                'access': access,
                'age': age,
                'floor': floor.text,
                'fee': fee.text,
                'management_fee': management_fee.text,
                'deposite': deposite.text,
                'gratuity': gratuity.text,
                'madori': madori.text,
                'menseki': menseki.text
            }
            d_list.append(d)


    # pprint(d_list[1])
# pprint(d_list[:2])

df = pd.DataFrame(d_list)
print(df.head())
print(df.shape)

print(len(df.title.unique()))

df.to_csv('test.csv', index=None, encoding='utf-8-sig')


# print(d)

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

