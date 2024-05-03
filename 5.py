with open('input.txt') as source, open('output.txt', 'w') as output:
    numbers = source.read().split('\n')
    try:
        fst = int(numbers[0])
        scnd = int(numbers[1])
        third = int(numbers[2])
        output.write(str(fst / scnd + third))
    except ValueError:
        output.write('data error')
    except ZeroDivisionError:
        output.write('division by 0')
