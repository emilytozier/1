#напишите строки файла в обратном порядке
fin=open('input_write.txt','w',encoding='utf8')
inf = open('input_1.txt', 'r', encoding='utf8')
s=inf.readlines()
print(''.join(s[::-1]), file=fin)
fin.close()
inf.close()