from simplified_scrapy import SimplifiedDoc, utils, req
res = req.get('https://stepik.org/media/attachments/lesson/266068/map2.osm')
xml = res.read().decode('utf-8')
doc = SimplifiedDoc(xml)
print(doc)
cnt=0
for node in doc.selects('node'):
    tag = node.selects('tag') # Find all nd
    if isinstance(tag, list):
        print('list')
        shop = tag.select('tag@k=shop') # Judge whether there is a tag with k = building
        if shop:
            cnt+=1
        print(cnt)