import csv


def write_csv(data):
	with open('writers.csv','a') as file:
		writer=csv.writer(file)
		writer.writerow([data['name'],data['surname'],data['age']])

def write_csv2(data):
	with open('writers2.csv','a') as file:
		order=['name','surname','age']
		writer=csv.DictWriter(file, fieldnames=order)
		writer.writerow(data)


def open_csv():
	with open('writers2.csv','r') as file:
		reader=csv.DictReader(file)
		for i in reader:
			print(i)


d1={'name':'Pert','surname':'Romanov','age':44}
d2={'name':'Vlodimir','surname':'Lenin','age':34}
d3={'name':'Lev','surname':'Tolstoy','age':74}

d_list=[d1,d2,d3]


open_csv()