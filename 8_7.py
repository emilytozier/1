
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml

cnt = 0
for node in soup.find_all('node'): # идем по всем тэгам way
    for tag in node('tag'):
        if tag['k']=='amenity' and tag['v']=='fuel':
            cnt +=1
print(cnt)