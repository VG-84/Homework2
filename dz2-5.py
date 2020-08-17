# dz 2-6

product_template = {
    'Название': ('Имя товара', str),
    'Цена': ('Стоимость товара', int),
    'Количество': ('Количество товара', int),
    'Еденица': ('Еденица измерения', str),
}
next_enter = True
auto_inc = 1
product_list = []
while next_enter:
    product = {}
    for key, value in product_template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f'{e}\nНеверное значение')
                continue
            product[key] = user_value
            break
    product_list.append((auto_inc, product))
    auto_inc +=1
    while True:
        next_add = input('Добавить еще продукт? Да/Нет\n')
        if next_add.lower() in ('Да', 'Нет'):
            next_enter = next_add.lower() == 'Да'
            break
        else:
            print('Неверный ввод')
print(product_list)
product_analytics = {}
for key in product_template:
    result = []
    for itm in  product_list:
        result.append(itm[1][key])
    product_analytics[key] = result
print(product_analytics)