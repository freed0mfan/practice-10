import os

os.mkdir('simple')
with open('input.txt', 'r') as source, open('simple/output.txt', 'a', encoding='utf-8') as output:
    data = source.read().split('\n')
    for i in range(len(data)):
        if i % 2 == 0:
            output.write(data[i] + '\n')
