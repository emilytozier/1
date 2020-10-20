#Скачайте с помощью скрипта область карты OSM, где минимальная широта равна 55.5586, минимальная долгота 37.5649, максимальная широта 55.5728, максимальная долгота 37.5803.

#Чтобы вспомнить, как добыть адрес api, который возвращает вам нужный кусок карты, пройдите по ссылке https://www.openstreetmap.org/export, 
#включите режим разработчика в браузере (ctrl+shift+i), откройте вкладку "Network", затем выберите слева Manually select a different area, выберите какую-нибудь область и 
#нажмите кнопку Export. Во вкладке Network появится адрес ссылки, по которой добывается xml файл. Исправьте в нем координаты на данные в условии задачи и вы получите адрес того файла, который нужно сдать на проверку.

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve
#

urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=37.5649%2C55.5586%2C37.5803%2C55.5728', 'n/map.osm')
xml=open('n/map.osm','r', encoding='utf=8').read()
soup=BeautifulSoup(xml, 'lxml')
print(soup)
