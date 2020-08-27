import random
import sys

def func (number, digit_1, count=0):
    BASE = 10
    if number % BASE == number:
        if number == digit_1:
            return count + 1, locals()
        else:
            return count, locals()
    else:
        if number % BASE == digit_1:
            return func(int(number / BASE),digit_1, count + 1)
        else:
            return func(int(number / BASE),digit_1, count)

def count_number_2 (num, digit):
    count_1 = 0
    MAX_ITEM = 10000000000
    for i in range(1, num + 1):
        ans = random.randint(1, MAX_ITEM)
        rec, opt  = func(ans, digit)
        count_1 += rec
    variables = {**locals(), **opt}
    return count_1, variables


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
        if not isinstance(val, dict):
            res +=show(val)
    print(f'Затрачено памяти - {res}')

count_memory(count_number_2(100,6))