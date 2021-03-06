#В этой статье есть теги code, которыми выделяются конструкции на языке Python. 
#Вам нужно найти все строки, содержащиеся между тегами <code> и </code> и найти те строки, которые встречаются чаще всего и вывести их в алфавитном порядке, разделяя пробелами.
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import re

resp = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html ")
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
