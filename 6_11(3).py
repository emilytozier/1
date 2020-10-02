mint = (10000, '','')
import csv
with open('tk4.csv', 'w') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    with open('input_4.csv', 'r', encoding='utf8') as fin:
        _, *prods = fin.readline().rstrip('\n').split(';')#read 1st string with names of products with deleted backspaces
        for line in fin: #read second and other strings, separating shop and massive of prices
            shop, *prices = line.rstrip('\n').split(';')
            for i, price in enumerate(prices):#assign prods name to price and put shop in accordance
                curt = (int(price), prods[i], shop)
                mint = min(mint, curt)
    print(mint[1], mint[2], sep='\n', file=output_file)
