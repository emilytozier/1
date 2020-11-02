#В этой задаче достаточно обернуть в функцию то, что делает предыдущая и вызвать подсчет 
#числа внутренних ссылок для двух статей: https://stepik.org/media/attachments/lesson/258943/Moscow.html и https://stepik.org/media/attachments/lesson/258944/New-York.html

from urllib.request import urlopen

from bs4 import BeautifulSoup

def getilinks(url):
    respponse = urlopen(url)
    html = respponse.read().decode('utf-8')
    soup = BeautifulSoup(html)
    links = set()
    # создаем множество исключений
    exp = set(['#', 'http://:', 'https://', '//'])
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            s = link.get('href')
            if s.startswith('/w') and ':' not in s:
                flag = True
                for now in exp:
                    if s.startswith(now):
                        fiag = False
                if flag:
                    links.add(link.get('href'))
    return links

mos=getilinks('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/Moscow.html')
ny=getilinks('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/New-York%20(1).html')
print(len(mos & ny))
