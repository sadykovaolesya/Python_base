from collections import defaultdict

count_companeis = int (input('Введите количество компаний: '))

dict_of_lists = defaultdict(int)
avr = 0
for _ in range(count_companeis):
    name = input('Введите название организации: ')
    for i in  range(4):
        profit = int (input(f'Введите прибыль за {i + 1} квартал: '))
        dict_of_lists[name] += profit
    avr += dict_of_lists[name]
avr = avr/count_companeis
print(f'Средняя прибыль - {avr}')

for name in dict_of_lists:
    if (dict_of_lists[name]) > avr:
        print(f'{name} - Прибыль выше среднего')
    else:
        print(f'{name} - Прибыль ниже среднего')


