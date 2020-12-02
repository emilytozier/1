from xml.dom import minidom
xmldoc=minidom.parse('books.xml')
a_list=xmldoc.getElementsByTagName('person')
print(len(a_list))
print(a_list[0].attributes['name'].value)
for i in a_list:
	print(i.attributes['name'].value)