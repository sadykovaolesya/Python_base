import random

SIZE = 10
MIN_ITEM = 10
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_new = [i for i, number in enumerate(array) if number % 2 == 0]
print(array_new)

