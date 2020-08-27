import random
import sys

def count_number_3 (num, digit):
    MAX_ITEM = 10000000000
    a = ''
    for i in range(1, num + 1):
        ans = str(random.randint(1, MAX_ITEM))
        a += ans
    n = digit
    n = str (digit)
    return a.count(n), locals()

def show(x, size = 0):
    size = sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size

def count_memory(func):
    res = 0
    for key, val in func[1].items():
        res +=show(val)
    print(f'Затрачено памяти - {res}')

count_memory(count_number_3(1000,6))