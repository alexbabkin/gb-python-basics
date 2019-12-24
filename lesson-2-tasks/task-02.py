#
# Task 2.
#

lst = []
while True:
    user_input = input('Введите следующий элемент списка или нажмите enter для завешения ввода: ')
    if user_input == '':
        break
    lst.append(user_input)

indexes = range(len(lst))
for i in indexes[1::2]:
    lst[i-1], lst[i] = lst[i], lst[i-1]

for e in lst:
    print(e)
