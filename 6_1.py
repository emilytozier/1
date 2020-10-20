#количество уникальных слов в тексте
with open('input.txt') as fin:
    for line in fin:
        l = len(set(line.split()))
    fin.close()
    print(l)
