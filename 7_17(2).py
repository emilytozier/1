
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re

response = urlopen('https://stepik.org/media/attachments/lesson/258944/New-York.html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table',attrs={'class':'wikitable collapsible collapsed'})
table_city_and_state = tables[1]
print(table_city_and_state)