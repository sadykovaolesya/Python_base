import random

SIZE = 100
MIN_ITEM = -15
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_el = array[0]
pos = 0

for i, number in enumerate(array):
    if number < 0:
        if max_el >= 0:
            max_el = number
            pos = i
        if max_el < number:
            max_el = number
            pos = i
if max_el >= 0:
    print('Отрицательных элементов нет')
else:
    print(f'{max_el} на позиции {pos}')

