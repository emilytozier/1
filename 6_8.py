#работа в csv файле -отстортировать компании по средней з/п, когда даны в строчках инфа на каждого сотрудника
inn = open('t.csv', 'w')
import csv
d1 = {}
with open('input_1.csv') as File:
    reader = csv.reader(File, delimiter=';')

    for row in reader:
        a = row[0]
        if a not in d1:
            d1[a] = 0
        d1[a] += 1

import csv



dd = {}
with open('input_1.csv') as File:
    reader = csv.reader(File, delimiter=';')
    for row in reader:
        a = row[0]
        b = int(row[1])
        dd[a] = dd.get(a,0)+int(b)


import csv

d = {}

with open('input_1.csv') as File:
    reader = csv.reader(File, delimiter=';')
    for row in reader:
        a = row[0]
        b = dd[a] / d1[a]
        d[a] = b
print(d)
import operator
sorted_x = sorted(d.items(), key=operator.itemgetter(1))

for z in sorted_x:
    ss = z[0]
    print(ss, file=inn)
