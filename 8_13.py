from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve

response= urlopen(' https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml=response.read().decode('utf8')
soup=BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
        if way.find_all('nd')[0]==way.find_all('nd')[-1]:
            for tag in way('tag'):
                if tag['k'] == 'building':
                    print(way['id'])
                    for nd in way.find_all('nd'):
                        print(nd['ref'], end=' ')
                    print()