
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