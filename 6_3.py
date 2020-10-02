#напишите сумму чисел в каждой строке
with open('input_2.txt') as t:
    print(*(sum(map(int, line.split())) for line in t.readlines()), sep=' ')
