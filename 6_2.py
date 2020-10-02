#напишите все слова файла в порядке наибольшего встречания и по алфавиту если встречаются одинаково раз
from collections import Counter
from typing import List, Any

#fin = open('input.txt', 'r+', encoding='utf8')
f=open('input_write.txt','w',encoding='utf8')
#words = []

#s = fin.read().split()
elements = []
with open('input.txt') as inf:
    for line in inf:
        elements.extend(line.split())
#for line in s:
    #words.extend(s)

counter = Counter(elements)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print(' '.join(words), file=f, end='')
f.close()
inf.close()

