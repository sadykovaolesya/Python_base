import random
import timeit
import cProfile

def count_number_3 (num, digit):
    MAX_ITEM = 10000000000
    a = ''
    for i in range(1, num + 1):
        ans = str(random.randint(1, MAX_ITEM))
        a += ans
    n = digit
    n = str (digit)
    return a.count(n)

print(timeit.timeit('count_number_3 (5, 1)', number=1000, globals=globals()))     #0.010892500000000006
print(timeit.timeit('count_number_3 (20, 1)', number=1000, globals=globals()))    #0.0349237
print(timeit.timeit('count_number_3 (50, 1)', number=1000, globals=globals()))    #0.0901121
print(timeit.timeit('count_number_3 (100, 1)', number=1000, globals=globals()))   #0.19970109999999996
print(timeit.timeit('count_number_3 (500, 1)', number=1000, globals=globals()))   #1.0698233
print(timeit.timeit('count_number_3 (1000, 1)', number=1000, globals=globals()))  #2.130966

cProfile.run('count_number_3(5, 1)')
#1    0.000    0.000    0.000    0.000 Task1_3.py:5(count_number_3)
cProfile.run('count_number_3(20, 1)')
#  1   0.000    0.000    0.000    0.000 Task1_3.py:5(count_number_3)
cProfile.run('count_number_3(50, 1)')
#1    0.000    0.000    0.000    0.000 Task1_3.py:5(count_number_3)
cProfile.run('count_number_3(100, 1)')
#1     0.000    0.000    0.000    0.000 Task1_3.py:5(count_number_3)
cProfile.run('count_number_3(500, 1)')
#  1     0.001    0.001    0.002    0.002 Task1_3.py:5(count_number_3)
cProfile.run('count_number_3(1000, 1)')
# 1   0.001    0.001    0.003    0.003 Task1_3.py:5(count_number_3)
