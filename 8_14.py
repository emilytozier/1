#Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

#Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node), 
#среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.

#Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way. 
#Во второй выведите список кортежей, содержащих координаты (широту и долготу) всех node, входящих в этот way. 
#Для этого удобно в первой задаче к предыдущему видео сохранить все координаты в словарь, где ключом явлеятся id нода, и совместить ее с последней задачей

#Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

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




