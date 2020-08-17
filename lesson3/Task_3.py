import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_el = array[0]
max_el = array[0]

for i, number in enumerate(array):
    if max_el < array[i]:
        max_el = array[i]
    if min_el > array [i]:
        min_el = array [i]

array[array.index(max_el)] = min_el
array[array.index(min_el)] = max_el

print(array)


