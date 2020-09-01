# Решена только Task3 , Task1 и Task2 недоделаны

import random

MIN_ITEM = -100
MAX_ITEM = 100
SIZE = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def bubble_sort(arr):
    n = 1
    spam = 0
    while n < len(array):
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                spam += 1
        print(array)
        n += 1
    print(spam)



bubble_sort(array)
