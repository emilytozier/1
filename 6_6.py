#напишите самую длинную строку в коде
inf=open('input_4.txt','r',encoding='utf8')
s=inf.readlines()

maxlen = max(len(line)for line in s)
with open('input_write.txt', 'w') as out:
    out.write(*filter(lambda line: len(line) == maxlen, s))
out.close()
inf.close()
jk