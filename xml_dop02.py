from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)
#tree=ElementTree.ElementTree(file='books.xml')

root=tree.getroot()

#print(root)
#print(root.tag)
#print(root.attrib)
#print(root.text)

#for i in root.iterfind('.'):
#	print(i.tag)

#for i in root.iterfind('.//'):
#	print(i.tag)

for i in root.iterfind('./book//'):
	print(i.tag)