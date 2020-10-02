import requests
from bs4 import BeautifulSoup


url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

num_way = len(soup.select('way'))
#w = max(sorted(soup.select('way:has(nd)'), reverse=True, key=lambda tag: len(tag.select('nd'))))
w = max(sorted(soup.select('way:has(nd)'), reverse=True, key=lambda tag: int(tag['id'])), key=lambda tag: len(tag.select('nd')))
print('number of <way>:', num_way)
print('id:', w['id'])
print('quantity of <nd>:', len(w.select('nd')))