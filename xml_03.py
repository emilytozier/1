from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)
print(tree)

root=tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
print(root.text)

for i in root:
    print(i.tag, i.attrib)

print(root[0][0].text)

for i in root:
	for j in i:
		print(j.tag,j.attrib)

