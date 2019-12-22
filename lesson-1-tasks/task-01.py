#
# Task 1.
#
# When we expects a number for the user input, it makes seance to have a function with validation, like this:
#
# def get_user_input_int():
#    while True:
#        input_var = input('Веедите число: ')
#        try:
#            input_var_int = int(input_var)
#            return input_var_int
#        except ValueError:
#            print('Введено некорректное значение')
#
# But for this lesson we assume that user input is always correct
#
var1 = 1
var2 = 'My variable'
var3 = True

print(f'var1 = {var1}, var2 = {var2}, var3 = {var3}')

input_var_str = input('Введите строку: ')
input_var_int = int(input('Введите число: '))

print(f'input_var_str = {input_var_str}, input_var_int = {input_var_int}')
