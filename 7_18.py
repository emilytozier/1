#преобразовать 2ую таблицу из 17 задания в csv таблицу, где ячейки через запятую
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re

response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/New-York%20(1).html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table',attrs={'class':'wikitable collapsible collapsed'})
lines = tables[1](['tr'])
cells=[]
s=[]
for line in lines:
    cells+=([line.text])
for each in cells:
    s.append(str(each).strip().split('\n'))
for i in s:
    print(','.join(i))

