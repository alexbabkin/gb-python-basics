#
# Task 5.
#
# IMPORTANT! Initial list must already be sorted
#
#

lst = [7, 5, 4, 4, 2]

user_input = int(input('Введите число: '))

if user_input > max(lst):
    lst.insert(0, user_input)
else:
    idx = len(lst) - 1
    
    while idx >= 0:
        if user_input <= lst[idx]:
            lst.insert(idx+1, user_input)
            break
        idx -= 1

print('Новый рейтинг: ')
for el in lst:
    print(el)
