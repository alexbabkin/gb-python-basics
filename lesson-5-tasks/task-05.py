#
# Task 5
#

from random import randint

with open('files/task5-output.txt', 'w') as f:
    for i in range(11):
        f.write(f'{randint(1, 100)} ')

with open('files/task5-output.txt') as f:
    numbers = f.read().split()

print(sum(map(int, numbers)))
