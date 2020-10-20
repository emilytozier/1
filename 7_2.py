##html-код на питоне: html-файл, в котором будет таблица размером 10 на 10, которая должна содержать таблицу умножения для чисел от 1 до 10
with open('new2.html', 'w', encoding='utf8') as new_file:
    print('<html>', '<body>', '<table>', file=new_file, sep='\n')
    for i in range(1, 11):
        print('<tr>', file=new_file)
        for j in range(1, 11):
            print('<td>', str(i*j), '</td>', file=new_file)
        print('</tr>', file=new_file)
    print('</table>', '</body>', '</html>', file=new_file, sep='\n')
