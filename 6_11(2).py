#ищет в csv файле цены самых дешевых продуктов и выводит название магазина (из столбца) и название продукта(из 1 строки) для самого дешевого продукта (где название магазина первое в алфавитном порядке , где название продукта первое в алф.порядке)
L = []
import csv
with open('tk.csv', 'w') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    with open('input_4.csv', 'r', encoding='utf8') as f:
        products = f.readline().strip('\n').split(';')[1:]
        for line in f:
            shop, *prices = line.strip('\n').split(';')
            for i, price in enumerate(prices):
                L.append((shop, products[i], int(price)))  # add (t)uple

    # Sort by price, shop, product and get data from first item of L.
        shop, product, _ = sorted(L, key=lambda t: (t[2], t[0], t[1]))[0]
    print(product, shop, sep='', file=output_file)