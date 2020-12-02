from xml.etree import ElementTree
file01=open('books.xml','r')
tree=ElementTree.parse(file01)

root=tree.getroot()

print(root)
print(root.tag)
print(root.attrib)
print(root.text)

book=ElementTree.Element('book')
number=ElementTree.SubElement(book,'number')
year=ElementTree.SubElement(book,'year').set('year','2017')
pages=ElementTree.SubElement(book,'pages').set('pages','100')

number.set('pages','50')

root.append(book)

book=ElementTree.Element('book')
number=ElementTree.SubElement(book,'number').set('number','01')
year=ElementTree.SubElement(book,'year').set('year','1917')
pages=ElementTree.SubElement(book,'pages').set('pages','300')

#number.set('pages','50')

root[0].append(book)

tree.write('books4.xml')