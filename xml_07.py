from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)

root=tree.getroot()

print(root)
print(root.tag)
print(root.attrib)
print(root.text)

for i in root.findall('book'):
	pages=int(i.find('pages').text)
	print(pages)
	if pages >100:
		root.remove(i)


tree.write('books3.xml')
