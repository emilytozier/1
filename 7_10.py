#Вам необходимо обработать ее с помощью BeautifulSoup и подсчитать все внутренние ссылки, которые не содержат в себе двоеточия 
#(не являются ссылкой на техническую статью в википедии) и не начинаются с символа #.
#Под ссылкой понимается содержимое аттрибута href тега a. Ссылка называется внешней, если она ведет на другой сайт (т.е. начинается с http:// или https://). 
#Все остальные ссылки являются внутренними.В качестве ответа выведите количество внутренних ссылок, удовлетворяющих условию.

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
