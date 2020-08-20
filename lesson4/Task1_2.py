import random
import timeit
import cProfile

def func (number, digit, count=0):
    BASE = 10
    if number % BASE == number:
        if number == digit:
            return count + 1
        else:
            return count
    else:
        if number % BASE == digit:
            return func(int(number / BASE),digit, count + 1)
        else:
            return func(int(number / BASE),digit, count)


def count_number_2 (num, digit):
    count = 0
    MAX_ITEM = 10000000000
    for i in range(1, num + 1):
        ans = random.randint(1, MAX_ITEM)
        count += func(ans, digit)
    return count



print(timeit.timeit('count_number_2 (5, 1)', number=1000, globals=globals())) #0.036134799999999995
print(timeit.timeit('count_number_2 (20, 1)', number=1000, globals=globals())) #0.1489973
print(timeit.timeit('count_number_2 (50, 1)', number=1000, globals=globals())) #0.364535
print(timeit.timeit('count_number_2 (100, 1)', number=1000, globals=globals())) #0.7155104
print(timeit.timeit('count_number_2 (500, 1)', number=1000, globals=globals())) #3.4476328999999994
print(timeit.timeit('count_number_2 (1000, 1)', number=1000, globals=globals())) #6.8327057


cProfile.run('count_number_2(5, 1)')
#1    0.000    0.000    0.000    0.000 Task1_2.py:19(count_number_2)
cProfile.run('count_number_2(20, 1)')
# 1    0.000    0.000    0.000    0.000 Task1_2.py:19(count_number_2)
cProfile.run('count_number_2(50, 1)')
#1  0.000    0.000    0.001    0.001 Task1_2.py:19(count_number_2)
cProfile.run('count_number_2(100, 1)')
#1    0.000    0.000    0.002    0.002 Task1_2.py:19(count_number_2)
cProfile.run('count_number_2(500, 1)')
# 1     0.001    0.001    0.013    0.013 Task1_2.py:19(count_number_2)
cProfile.run('count_number_2(1000, 1)')
# 1     0.001    0.001    0.013    0.013 Task1_2.py:19(count_number_2)