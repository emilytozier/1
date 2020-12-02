import csv

def w_csv(data):
    with open('writers.csv','a') as file:
        writer = csv.writer(file)
        #order=['name','surname','age']
        #writer=csv.DictWriter(file, fieldnames=order)
        writer.writerow([data['name'],data['surname'],data['age']])

def o_scv():
    with open('writers.csv') as file:
        order=['name','surname','age']
        reader=csv.DictReader(file, fieldnames=order)
        for i in reader:
            print(i)



o_scv()