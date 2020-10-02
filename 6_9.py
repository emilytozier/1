inn = open('tk.csv', 'w')

import csv

with open('input_2.csv') as File:
    reader = csv.reader(File, delimiter=';')
    d =dict()

    for row in reader:
        a = row[0]
        b = row[1]
        a, b = b, a
        print(a, b, sep=';', file=inn, end='')




