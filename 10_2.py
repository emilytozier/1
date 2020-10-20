import xmltodict

with open('map (2).osm') as fd:
    doc = xmltodict.parse(fd.read())
fin.close()


code=None
for artikel in xml['tag']:
    if artikel['shop']:
        code = artikel['shop']
    if isinstance(tag, list):
        print('list')
    elif isinstance(tag, dict):
        print('dict')
    print(code)
