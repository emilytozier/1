#В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. Ноды могут не только обозначать какой-то точечный объект, 
#но и входить в состав way (некоторой линии, возможно замкнутой) и не иметь собственных тегов. 
#Для доступного по ссылке https://stepik.org/media/attachments/lesson/245681/map2.osm фрагмента карты посчитайте, сколько 
#всего тегов node не содержат в себе ни одного тега tag (первое число в ответе), а сколько содержит хотя бы один тег tag (второе число в ответе). Числа введите через пробел.

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
