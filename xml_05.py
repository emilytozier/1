from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)

root=tree.getroot()

print(root)
print(root.tag)
print(root.attrib)
print(root.text)

for i in root.findall('book'):
    bookpages=i.find('pages').text
    bookpersons=i.findall('person')
    name=i.get('name')
    print(name)
    print(bookpages)
    print(bookpersons)