with open('input.txt', encoding='utf-8') as source, open('output.txt', 'w') as output:
    output.write(source.read().upper())
