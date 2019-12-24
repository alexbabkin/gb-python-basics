#
# Task 4.
#

user_input_str = input('Введите строку: ')

for i, word in enumerate(user_input_str.split(), start=1):
    print(i, word[:10:])
