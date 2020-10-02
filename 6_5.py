#напишите кол-во букв, строк, и слов в тескте
letters = words = lines = 0  # counters
inword = False
with open('input_3.txt', 'r') as f:
    for line in f:
        for char in line:
            if char.isalpha():
                letters += 1
                if not inword:
                    inword = True
                    words += 1
            else:
                inword = False

        lines += 1

print('Input file contains:')
print(letters, 'letters')
print(words, 'words')
print(lines, 'lines')