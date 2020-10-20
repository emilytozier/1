from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/2.html")
html = resp.read().decode('utf8')
#soup = BeautifulSoup(html, 'html.parser')


def olga_kuz9_refactor(): # удобно вложить задание в функцию
    soup = BeautifulSoup(html, 'html.parser') # не забываем парсер
    data={}
    for code in soup.find_all ('code'):
        s = code.text # содержимое тега без срезов
        data[s] = data.get(s, 0) + 1 # счетчик через get без if
    L = max(data.values()) # max сразу из значений словаря
    res = [] # список для результатов
    for tup in data.items(): # без перевода словаря в список
        if tup[1] == L: # Если 2-ой элемент кортежа равен макс
            res.append(tup[0]) # + 1-й элемент кортежа в результаты
    return ' '.join(sorted(res)) # Сортируем результаты и 
    # объединяем элементы через пробел
print(olga_kuz9_refactor()) # Печатаем результат