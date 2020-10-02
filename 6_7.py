
#напечатать "зеркальное" отражение строк
fin=open('input_write.txt','w',encoding='utf8')
inf = open('input_5.txt', 'r', encoding='utf8')



with open('input_5.txt') as f:
    for text in reversed(f.read()):
        print(text, file=fin, end='')


fin.close()
inf.close()
