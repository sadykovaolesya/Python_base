import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
max_el_count = 0
el = array[0]
for i in array:
    count = 0
    for j in array:
        if i == j:
            count += 1
    if max_el_count < count:
        max_el_count, el = count, i
print(f'{el} встречается {max_el_count} раз')

