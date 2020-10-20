

from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/2.html")
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

def mykey(x):
    return x[1] # Какое поле сортировать

data={}
for code in soup.find_all ('code'):
    s = str(code)[6:-7] #
    print(s)
    if s not in data:
        data[s]=0
        data[s] += 1
        L=max(data.items(), key = mykey)[1]
        print(L)
        data=list(data.items())
        for i in range(1,len(data)):
            if data[i][1] == L:
                print(data[i][0], sep='\n')