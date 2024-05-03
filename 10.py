def day_of_year(date):
    index = {'01': 0, '02': 1, '03': 2, '04': 3, '05': 4, '06': 5, '07': 6, '08': 7, '09': 8,
             '10': 9, '11': 10, '12': 11}
    month_duration = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = index[date[-2:]]
    if date[0] == 0:
        day = int(date[1])
    else:
        day = int(date[0:2])
    return sum(month_duration[0:month]) + day


with open('input.txt', 'r') as source, open('output.txt', 'a') as output:
    data = source.read().split('\n')
    today = day_of_year(data[0])
    n = int(data[1])
    cells = []
    dates = []
    for x in data[2:]:
        cells.append(x.split(' ')[0])
        dates.append(x.split(' ')[1])
    storage_start = []
    for date in dates:
        storage_start.append(day_of_year(date))
    storage_time = []
    for start in storage_start:
        storage_time.append(today - start)
    for time in storage_time:
        if time > 3:
            output.write(cells[storage_time.index(time)] + '\n')
