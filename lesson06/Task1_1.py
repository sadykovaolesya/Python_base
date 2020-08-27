import random
import sys

#64-bitб OS, PCh
# Task1_1 = Затрачено памяти - 100
# Task1_2 = Затрачено памяти - 158
# Task1_3 = Затрачено памяти - 1132
# Task1_3 потребляет больше памяти, но работает быстрее, Task1_1 потребляет меньше памяти, но работает немного медленее,
# вслучае если оперативной памяти недостаточноб целесобразней использовать Task1_1

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
    return count, locals()


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

count_memory(count_number(100,6))