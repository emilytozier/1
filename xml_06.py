from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)

root=tree.getroot()

print(root)
print(root.tag)
print(root.attrib)
print(root.text)

#iter ищет среди потомков number

for i in root.iter('number'):
	new_number=int(i.text)+1
	i.text=str(new_number)
	i.set('updated','2017')

tree.write('books2.xml')
