from urllib.request import urlopen

from bs4 import BeautifulSoup

def getilinks(url):
    respponse = urlopen(url)
    html = respponse.read().decode('utf-8')
    soup = BeautifulSoup(html)
    links = list()
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
                    links.append(link.get('href'))
    return links

print(len(getilinks('file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/Moscow.html')))
