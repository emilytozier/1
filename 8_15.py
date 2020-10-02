from simplified_scrapy import SimplifiedDoc, utils, req
res = req.get('https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml = res.read().decode('utf-8')
doc = SimplifiedDoc(xml)
import math
import operator

def getsqr(coordlist):
     baselat = coordlist[0][0]
     baselon = coordlist[0][1]
     degreelen = 111300
     newcoord = []
     for now in coordlist:
          newcoord.append(((now[0] - baselat) * degreelen, (now[1] - baselon) * degreelen * math.sin(baselat)))
     sqr = 0
     for i in range(len(newcoord) - 1):
          sqr += newcoord[i][0] * newcoord[i + 1][1] - newcoord[i + 1][0] * newcoord[i][1]
     sqr += newcoord[-1][0] * newcoord[0][1] - newcoord[0][0] * newcoord[-1][1]
     return abs(sqr)


dic = {}
for node in doc.nodes:
    lat = float(node['lat'])
    lon = float(node['lon'])
    id = node['id']
    dic[id] = (lat, lon)
cro={}
for way in doc.selects('way'):
    nds = way.selects('nd>ref()') # Find all nd
    building = way.select('tag@k=building') # Judge whether there is a tag with k = building
    if nds[0]==nds[-1] and building:
        #print(way['id'])
        coordlist= [dic[nd] for nd in nds if nd in dic]

        cro[way['id']]=getsqr(coordlist)
print(max(cro, key=lambda key: cro[key]))