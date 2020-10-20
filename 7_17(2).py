
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re

response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/New-York%20(1).html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table',attrs={'class':'wikitable collapsible collapsed'})
table_city_and_state = tables[1]
print(table_city_and_state)