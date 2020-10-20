#Вручную откройте скаченный файл с помощью 
#текстового редактора и найдите в нём тэг tag с атрибутом k="public_transport" в node с id равным 203573042 (удобно поискать это число поиском в текстовом редакторе).
from bs4 import BeautifulSoup

xml = open('map2.osm', 'r', encoding='utf8').read()

soup = BeautifulSoup(xml, 'lxml')
print(soup)
