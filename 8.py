month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
         'декабрь']
month_duration = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
with open('input.txt', 'r') as source, open('output.txt', 'a', encoding='utf-8') as output:
    data = source.read().split('\n')
    steps = list(map(int, data))
    days = 0
    for line in source:
        days += 1
    if days == 366:
        month_duration[1] += 1
    for i in range(12):
        start = sum(month_duration[0:i])
        stop = start + month_duration[i] + 1
        month_steps = sum(steps[start:stop])
        average = month_steps / month_duration[i]
        output.write(f'Среднесуточное количество шагов за {month[i]}: {round(average)}\n')
