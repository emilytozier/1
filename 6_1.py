#количество уникальных слов в тексте
with open('input (1).txt') as fin:
    for line in fin:
        l = len(set(line.split()))
    fin.close()
    print(l)
