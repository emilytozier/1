#!/usr/bin/python3
from urllib.request import urlopen, urlretrieve
import re

from bs4 import BeautifulSoup

resp = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html")
html = resp.read().decode('utf8')
soup = BeautifulSoup(html, 'html.parser')




strings = soup.find_all(string=re.compile('C++'))

for txt in strings:
        print(" ".join(txt.split()))