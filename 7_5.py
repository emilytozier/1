#с помощью скрипта на Питоне и посчитайте, какой язык упоминается чаще Python или C++ (ответ должен быть одной из этих двух строк)
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html")
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
