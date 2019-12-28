#
# Task 1.
#


def divide_numbers(num, denom):
    if denom == 0:
        print('Деление на ноль запрещено')
        return
    return num / denom


numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))

result = divide_numbers(numerator, denominator)
if result is not None:
    print(f'Результат деления {result}')
