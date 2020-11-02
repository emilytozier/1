#В файле https://stepik.org/media/attachments/lesson/209723/5.html находится одна таблица. Просуммируйте все числа в ней. 
#Теперь мы не только добавили разных тегов для изменения стиля отображения, но и сделали невалидный HTML-код 
#(правда, браузеры его отображают, а вот с BeautifulSoup могут быть проблемы). Невалидный HTML-код - не редкость в интернете, надо учиться работать и с этим.
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re
import html5lib

response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/5.html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html5lib')# для невалидного кода

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
