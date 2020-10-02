#ищет в csv файле цены самых дешевых продуктов и выводит название магазина (из столбца) и название продукта(из 1 строки) для всех самых дешевых продуктов
import csv
with open('tk4.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter=';')
    with open('input_4.csv', 'r', encoding='utf8') as File:
        text = File.read()
        name_shop = list(map(lambda s: s.split(';')[0], text.splitlines()[1:]))
        name_product = text.splitlines()[0].split(';')[1:]
        data = list(map(lambda s: s.split(';')[1:], text.splitlines()[1:]))

        product = data
        shops_and_prices = [(num, list(map(int, row))) for num, row in enumerate(data, start=1)]
        best_row = min(shops_and_prices, key=lambda shop_and_price: min(shop_and_price[1], key=lambda val: val))
        best_price = min(best_row[1])
        res = [(rows[0], num) for rows in shops_and_prices if best_price in rows[1]
               for num, price in enumerate(rows[1], start=1) if price == best_price]
        for num_shop, num_product in res:
            print('{} - {}'.format(name_shop[num_shop - 1], name_product[num_product - 1]) + ' - ', best_price, file=output_file)


