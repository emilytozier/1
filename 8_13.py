#Вам дана область карты https://stepik.org/media/attachments/lesson/266078/mapcity.osm

#Пройдите по всем way в этой области, выделите среди них замкнутые (те, у которых совпадает ссылка на первый и последний node), 
#среди всех замкнутых выделите те, у которых установлен tag с ключом building и произвольным значением.

#Для каждого подходящего под условия way выведите две строки. В первой укажите одно число - id этого way. 
#Во второй перечислите через пробел id (ref) всех nd, входящих в этот way в том же порядке, в котором они перечисляются в файле.
#Выводить ответы для подходящих way нужно в том порядке, в котором они встречаются во входном файле

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from urllib.request import  urlopen, urlretrieve

response= urlopen(' https://stepik.org/media/attachments/lesson/266078/mapcity.osm')
xml=response.read().decode('utf8')
soup=BeautifulSoup(xml, 'lxml')

for way in soup.find_all('way'):
        if way.find_all('nd')[0]==way.find_all('nd')[-1]:
            for tag in way('tag'):
                if tag['k'] == 'building':
                    print(way['id'])
                    for nd in way.find_all('nd'):
                        print(nd['ref'], end=' ')
                    print()
