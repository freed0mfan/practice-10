with open('input.txt') as source, open('output.txt', 'w') as output:
    word = ''
    for line in source:
        word += line[0]
    output.write(word)
