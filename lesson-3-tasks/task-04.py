#
# Task 4.
#


def input_x():
    while True:
        try:
            num = float(input('Введите x: '))
        except ValueError:
            print('Неверный ввод')
        if num > 0:
            return num
        print('Неверный ввод')


def input_y():
    while True:
        try:
            num = int(input('Введите y: '))
        except ValueError:
            print('Неверный ввод')
        if num < 0:
            return num
        print('Неверный ввод')


def my_func1(x, y):
    return x ** y;


def my_func2(x, y):
    result = 1
    for i in range(1, abs(y) + 1):
        result *= x
    return 1/result


def my_func3(x, y):
    if y == 0:
        return 1
    return my_func3(x, y + 1) * 1/x


x = input_x()
y = input_y()
print(f'Вычисление степени с помощью функции my_func1: {my_func1(x, y)}')
print(f'Вычисление степени с помощью функции my_func2: {my_func2(x, y)}')
print(f'Вычисление степени с помощью функции my_func3: {my_func3(x, y)}')
