from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

resp = urlopen('https://stepik.org/media/attachments/lesson/245681/map2.osm') # скачиваем файл
xml = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(xml, 'xml') # делаем суп с помощью lxml
cnt = 0
x = 0

for node in soup.find_all('node'): # идем по всем нодам
    flag = False #сброс счетчика, по умолчанию нет тега, иначе он после первой ноды с тегом так и остается
    x +=1
    for tag in node('tag'):
        flag = True
    if flag:
        cnt += 1
print(x-cnt, cnt)