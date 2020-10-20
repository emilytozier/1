from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/1.html")
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')

cnt = 0
for tr in soup.find_all(string=re.compile("Python")):
    cnt += 1

cnt1 = 0
for tr in soup.find_all(string=re.compile("[cC]\+\+")):
    cnt1 += 1

if cnt>cnt1:
    print("Python")
else:
    print("C++")
