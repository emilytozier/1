from urllib.request import urlopen

from bs4 import BeautifulSoup


response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/New-York%20(1).html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table',attrs={'class':'wikitable collapsible collapsed'})

lines1 = tables[0](['tr'])
for line in lines1:
    print(','.join([cell.text.strip() for cell in line(['th', 'td'])]))
print('\n')
lines2 = tables[1](['tr'])
for line in lines2:
    print(','.join([cell.text.strip() for cell in line(['th', 'td'])]))
print('\n')
lines3 = tables[2](['tr'])
for line in lines3:
    print (','.join([cell.text.strip() for cell in line(['th', 'td'])]))