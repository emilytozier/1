import csv


def write_csv(data):
	with open('writers44.csv','a') as file:
		writer=csv.writer(file)
		#writer=csv.writer(file,delimiter=',')
		#writer=csv.writer(file, dialect='Excel')
		#writer.writerow((data['name'],data['surname'],data['age']))
		writer.writerow([data['name'],data['surname'],data['age']])


d1={'name':'Pert','surname':'Romanov','age':44}
d2={'name':'Vlodimir','surname':'Lenin','age':34}
d3={'name':'Lev','surname':'Tolstoy','age':74}

d_list=[d1,d2,d3]

for i in d_list:
	print(i)
	write_csv(i)