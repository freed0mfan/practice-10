with open('input.txt') as source, open('output.txt', 'w') as output:
    for line in source:
        if line[0].upper() == 'A':
            output.write(line)
