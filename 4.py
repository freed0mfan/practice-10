with open('input.txt') as source, open('output.txt', 'w') as output:
    for line in source:
        if len(line) > 20:
            output.write(line)
