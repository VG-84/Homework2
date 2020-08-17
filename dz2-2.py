# 2-2
data = input('Ввод данных')
data_list = data.split(' ')
numb = 0
len_numb = len(data_list) - 1
while numb < len_numb:
    data_list[numb], data_list[numb + 1] = data_list[numb + 1], data_list[numb]
    numb +=2
print(data_list)