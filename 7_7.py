#Вам необходимо обработать ее с помощью BeautifulSoup и вывести все ссылки, которые есть на этой странице, в том порядке как они встречались по одной в строке.
#Под ссылкой понимается содержимое аттрибута href тега a.
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/webpage.html")
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    if link.has_attr('href'):
                print(link.get('href'))
        #if s.startswith('wiki/C++'):
            #print(tr.get('href'))
