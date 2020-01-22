#
# Task 1
#

with open('files/task1-output.txt', 'w') as f:
    while True:
        line = input('Введите новую строку: ')
        if line == '':
            break
        else:
            f.write(line + '\n')
