from urllib.request import urlopen, urlretrieve
from simplified_scrapy import SimplifiedDoc, utils, req
res = req.get('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml = res.read().decode('utf-8')
doc = SimplifiedDoc(xml)
dic = {}
for node in doc.nodes:
    lat = node['lat']
    lon = node['lon']
    id = node['id']
    dic[id] = (lat, lon)

for way in doc.selects('way'):
    nds = way.selects('nd>ref()') # Find all nd
    building = way.select('tag@k=building') # Judge whether there is a tag with k = building
    if nds[0]==nds[-1] and building:
        print(way['id'])
        print([dic[nd] for nd in nds if nd in dic])




