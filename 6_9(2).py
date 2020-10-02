#поменять местами столбцы в csv файле и вывести в output файл
import csv

with open('tk.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    with open('input_2.csv') as input_file:
        reader = csv.reader(input_file, delimiter=';')
        for row in reader:
            a = row[0]
            b = row[1]
            a, b = b, a
            writer.writerow([a, b])
