word = input('Ввод строки')
for data, word in enumerate(word.split(' '), 1):
    print(f'{data}:{word[:10]}')