import  random
from collections import deque
from itertools import islice

m = 10
size = 2 * m + 1
MAX_ITEM = 100
MIN_ITEM = 0
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
min_el = min(array)
print(array)
index_midll = int(len(array)/2)

def midian_search(array, n_index, sum_count = 0, min_el = 0):
    if sum_count >= n_index + 1:
        return f'Медиана в массиве - {min_el}'
    arr = deque()
    count = 0
    min_el = min(array)
    for i in array:
        if i == min_el:
            arr.appendleft(i)
            count += 1
        else:
            arr.append(i)
    sum_count += count
    return midian_search(deque(islice(arr, count, None)),  n_index, sum_count, min_el)

print(midian_search(array,index_midll))

