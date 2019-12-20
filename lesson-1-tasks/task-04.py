#
# Task 4.
#

num = int(input('Введите число: '))

max_digit = 0
while num > 0:
    modulo = num % 10
    if modulo > max_digit:
        max_digit = modulo
    num = num // 10

print(f'Самая большя цифра в числе: {max_digit}')
