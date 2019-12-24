#
# Task 6.
#

parameters = {'название', 'цена', 'количество', 'еденицы'}

products = []
idx = 1

while True:
    is_new_product = input('Хотите ввести новый товар? (Д/Н) ')
    if is_new_product == 'Д' or is_new_product == 'д':
        product_props = {}
        for key in parameters:
            user_input = input(f'Введите {key}: ')
            product_props[key] = user_input
        products.append((idx, product_props))
        print('Товар добавлен')
        idx += 1
    elif is_new_product == 'Н' or is_new_product == 'н':
        print('Ввод закончен')
        break
    else:
        print('Неверный ввод, пожалуйста повторите...')

print('Введенные товары: ')
for product in products:
    print(product)

analytics = {}
for key in parameters:
    values = [product[1][key] for product in products]
    analytics[key] = list(set(values))

print('Аналитика по товарам: ')
print(analytics)
