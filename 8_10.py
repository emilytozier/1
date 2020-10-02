from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve
#

urlretrieve('https://www.openstreetmap.org/api/0.6/map?bbox=37.5649%2C55.5586%2C37.5803%2C55.5728', 'n/map.osm')
xml=open('n/map.osm','r', encoding='utf=8').read()
soup=BeautifulSoup(xml, 'lxml')
print(soup)