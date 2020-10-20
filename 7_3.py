#сгенерировать html-код на питоне и сдать на проверку html-файл, в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10. 
#Каждое число в таблице должно быть ссылкой на страницу http://<это число>.ru. Например, число 12 должно быть ссылкой на страницу http://12.ru
with open('new1.html', 'w', encoding='utf8') as new_file:
    print('<html>', '<body>', '<table>', file=new_file, sep='\n')
    for i in range(1, 11):
        print('<tr>', file=new_file)
        for j in range(1, 11):
            print('<td>', '<a href=http://' + str(i*j) + '.ru>', i * j, '</a>', '</td>', file=new_file)
        print('</tr>', file=new_file)
    print('</table>', '</body>', '</html>', file=new_file, sep='\n')
