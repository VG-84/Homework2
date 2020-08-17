# dz2-3

data_dict = {'winter': (12, 1, 2),
             'spring': (3, 4, 5),
             'summer': (6, 7, 8),
             'autumn': (9, 10, 11)}
month = int(input('Введи номер месяца'))
for key in data_dict.keys():
    if month in data_dict[key]:
        print(key)
