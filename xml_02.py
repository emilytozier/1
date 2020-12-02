from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)
print(tree)

root=tree.getroot()
print(root)
print(root.tag)
print(root.attrib)
print(root.text)

