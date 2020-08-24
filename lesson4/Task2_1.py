import timeit
import cProfile

def prime(n):
    i = 1
    list = [2]
    while True:
        i += 1
        if (i > 10) and ((i % 5 == 0) or (i % 2 == 0)):
            continue
        if len(list) > n - 1:
            break
        for j in list:
            if i % j == 0:
                break
        else:
            list.append(i)
    return list[n-1]

print(timeit.timeit('prime(10)', number=100, globals=globals())) #0.0010892000000000054
print(timeit.timeit('prime(100)', number=100, globals=globals())) #0.0492947
print(timeit.timeit('prime(1000)', number=100, globals=globals())) #4.5889049
print(timeit.timeit('prime(10000)', number=100, globals=globals())) #799.3280801000001

cProfile.run('prime(10000)')
# 1    6.877    6.877    6.885    6.885 Task2_1.py:4(prime)
