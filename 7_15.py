#В файле https://stepik.org/media/attachments/lesson/209723/4.html находится одна таблица. 
#Просуммируйте все числа в ней. Теперь мы добавили разных тегов для изменения стиля отображения.
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re

response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/4%20(1).html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

sum=0
# Retrieve all of the anchor tags
tags = soup('td')
for tag in tags:
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y)
    print(x)
    for i in x:
        i=int(i)
        sum=sum+i
print (sum)
