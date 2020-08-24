import timeit
import cProfile

def sieve(n):
    x =n * 11
    sieve_a = [i for i in range(x)]
    sieve_a[1] = 0
    index = 0
    for i in range(2, x):
        if sieve_a[i] != 0:
            j = i + i
            index += 1
            if index < n:
                while j < x:
                    sieve_a[j] = 0
                    j += i
            else:
                return sieve_a[i]

print(timeit.timeit('sieve(10)', number=100, globals=globals())) #0.0020953999999999973
print(timeit.timeit('sieve(100)', number=100, globals=globals())) #0.035874
print(timeit.timeit('sieve(1000)', number=100, globals=globals())) #0.4692475
print(timeit.timeit('sieve(10000)', number=100, globals=globals())) #5.8057391

cProfile.run('sieve(10000)')
#1    0.048    0.048    0.053    0.053 Task2.py:4(sieve)