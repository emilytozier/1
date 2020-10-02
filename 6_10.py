#цена самого дешевого товара
import csv
with open('input_3.csv') as File:
    reader = csv.reader(File, delimiter=';')

    for row in range(1):
        next(reader)
        print(min(min(row[1:]) for row in reader))











