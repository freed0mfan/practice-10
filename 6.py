with open('input.txt') as source, open('output.txt', 'w') as output:
    try:
        n = int(source.readlines()[0][0:-1])
        count = 0
        for line in source:
            count += 1
        if n == count - 1:
            output.write('YES')
        else:
            output.write('NO')
    except ValueError:
        output.write('ERROR')
