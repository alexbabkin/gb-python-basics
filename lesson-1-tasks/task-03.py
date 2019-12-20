#
# Task 3.
#

input_digit = None
while True:
    input_str = input('Введите цифру: ')
    if input_str == '0' or input_str == '1' or input_str == '2' or \
            input_str == '3' or input_str == '4' or input_str == '5' or \
            input_str == '6' or input_str == '7' or input_str == '8' or input_str == '9':
        input_digit = int(input_str)
        break
    print('Некорректный ввод, попробуйте еще раз')


result = int(input_digit) + \
         int(f'{input_digit}{input_digit}') + \
         int(f'{input_digit}{input_digit}{input_digit}')

print(f'{input_digit} '
      f'+ {input_digit}{input_digit} '
      f'+ {input_digit}{input_digit}{input_digit} '
      f'= {result}')
