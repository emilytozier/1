#напишите все слова файла в порядке наибольшего встречания и по алфавиту если встречаются одинаково раз
from collections import Counter
from typing import List, Any

<<<<<<< HEAD

f=open('input_write.txt','w',encoding='utf8')

=======
f=open('input_write.txt','w',encoding='utf8')
>>>>>>> e60b6cc6d2d1b82369faf81e00082ae9ec22eebf
elements = []
with open('input.txt') as inf:
    for line in inf:
        elements.extend(line.split())
<<<<<<< HEAD

=======
>>>>>>> e60b6cc6d2d1b82369faf81e00082ae9ec22eebf

counter = Counter(elements)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print(' '.join(words), file=f, end='')
f.close()
inf.close()

