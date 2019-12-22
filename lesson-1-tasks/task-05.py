#
# Task 5.
#

revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue > costs:
    profit = revenue - costs
    print(f'Фирама работает c прибылью. Размер прибыли: {profit}')
    profitability = profit / revenue
    print(f'Рентабельность: {profitability}')
    num_of_stuff = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {revenue / num_of_stuff}')
elif revenue < costs:
    print(f'Фирама работает в убыток. Размер убытка: {costs - revenue}')
else:
    print('Фирама работает в ноль')
