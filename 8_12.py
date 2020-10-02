from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve
response= urlopen(' https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml=response.read().decode('utf8')
soup=BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
    flag=False
    for tag in way('tag'):
        if tag['k'] == 'building':
            flag=True
    if flag:
        for nd in way('nd'):
            flag=False
            if way('nd')[0]==way('nd')[-1]:
                flag=True
        if flag:
            print(way['id'])
