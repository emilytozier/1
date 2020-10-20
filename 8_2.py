from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf8').read()

soup = BeautifulSoup(xml, 'lxml')
print(soup)
