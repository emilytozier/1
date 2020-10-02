from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve
#
from itertools import islice
response= urlopen('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml=response.read().decode('utf8')
soup=BeautifulSoup(xml, 'lxml')
dict= {}
for node in soup.find_all('node'):
    lat = node['lat']
    lon = node['lon']
    id = node['id']
    dict[id]=(lat,lon)
def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))
n_items = take(100, dict.items())
str=('\n'.join(' '.join(map(str, x)).replace("('","") for x in n_items))
str2=str.replace("', '", " ")
print(str2.replace("')",""))

