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