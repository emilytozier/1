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

#for i in root:
#	print(i.tag, i.attrib)

#for i in root:
#	print(i.tag,i.keys(),i.items())


#for i in root.iter():
#	print(i.tag, i.keys(),i.items(),i.text)


for i in root.iter('book'):
	print(i.tag, i.keys(),i.items(),i.text)



