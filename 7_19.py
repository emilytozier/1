from urllib.request import urlopen

from bs4 import BeautifulSoup


response = urlopen('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/New-York%20(1).html')
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table',attrs={'class':'wikitable collapsible collapsed'})
lines1 = tables[0](['tr'])
cells1=[]
s1=[]
for line in lines1:
    cells1+=([line.text])
for each in cells1:
    s1.append(str(each).strip().split('\n'))
for i in s1:
    print(','.join(i), sep='\n')

lines2 = tables[1](['tr'])
cells2=[]
s2=[]
for line in lines1:
    cells2+=([line.text])
for each in cells2:
    s2.append(str(each).strip().split('\n'))
for i in s2:
    print(','.join(i), sep='\n')

lines3 = tables[2](['tr'])
cells3=[]
s3=[]
for line in lines3:
    cells3+=([line.text])
for each in cells3:
    s3.append(str(each).strip().split('\n'))
for i in s3:
    print(','.join(i))