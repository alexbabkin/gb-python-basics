#
# Task 6.
#

start_dist = int(input('Введите начальную дистанцию: '))
desired_dist = int(input('Введите желаемую дистанцию: '))

if desired_dist < start_dist:
    print('Отдыхайте!')
else:
    current_dist = start_dist
    day = 1
    while True:
        print(f'{day}-й день: {round(current_dist, 2)} км')
        if current_dist >= desired_dist:
            break
        day += 1
        current_dist += current_dist * 0.1

    print(f'Ответ: на {day}-й день спортсмен достиг результата — не менее {desired_dist} км')
