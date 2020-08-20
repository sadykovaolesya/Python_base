#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
# Наиболее оптимальный вариант решения count_number_3 с использоваием встроенной функции count, наихудший варинт с использованием рекурсии count_number_2

import random
import timeit
import cProfile

def count_number (num, digit):
    BASE = 10
    count = 0
    MAX_ITEM = 10000000000
    for i in range(1, num + 1):
        ans = random.randint(1, MAX_ITEM)
        while ans > 0:
            if ans % BASE == digit:
                count += 1
            ans //= BASE
    return count

print(timeit.timeit('count_number (5, 1)', number=1000, globals=globals())) #0.016293100000000005
print(timeit.timeit('count_number (20, 1)', number=1000, globals=globals())) #0.0657936
print(timeit.timeit('count_number (50, 1)', number=1000, globals=globals())) #0.1952221
print(timeit.timeit('count_number (100, 1)', number=1000, globals=globals())) #0.36604719999999996
print(timeit.timeit('count_number (500, 1)', number=1000, globals=globals())) #1.9304742000000001
print(timeit.timeit('count_number (1000, 1)', number=1000, globals=globals())) #3.9049738

cProfile.run('count_number(5, 1)')
#1    0.000    0.000    0.000    0.000 Task1_1.py:5(count_number)
cProfile.run('count_number(20, 1)')
#  1    0.000    0.000    0.000    0.000 Task1_1.py:5(count_number)
cProfile.run('count_number(50, 1)')
#1    0.000    0.000    0.000    0.000 Task1_1.py:5(count_number)
cProfile.run('count_number(100, 1)')
#1    0.001    0.001    0.001    0.001 Task1_1.py:5(count_number)
cProfile.run('count_number(500, 1)')
#  1    0.002    0.002    0.003    0.003 Task1_1.py:5(count_number)
cProfile.run('count_number(1000, 1)')
# 1    0.002    0.002    0.005    0.005 Task1_1.py:5(count_number)



