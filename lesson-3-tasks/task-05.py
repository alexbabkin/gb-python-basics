#
# Task 5.
#


def parse_user_input(user_input):
    symbols = user_input.split()
    num_list = []
    for s in symbols:
        if s == 'q':
            return num_list, True
        num_list.append(float(s))
    return num_list, False


num_sum = 0
is_end = False
while not is_end:
    user_input = input('Введите числа разелленые пробелом, символ \'q\' является завершающим: ')
    num_list, is_end = parse_user_input(user_input)
    num_sum += sum(num_list)
    if is_end:
        print(f'Финальная сумма равна: {num_sum}')
    else:
        print(f'Текущая сумма равна: {num_sum}')
