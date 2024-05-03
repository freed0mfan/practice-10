with open('input.txt') as source, open('output.txt', 'w') as output:
    numbers = source.read().split('\n')
    for number in numbers:
        if int(number) != 100:
            output.write(number + '\n')
