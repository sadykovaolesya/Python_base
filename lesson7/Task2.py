import random

MIN_ITEM = 0
MAX_ITEM = 50
SIZE = 10
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def func_split(arr):
        n = int(len(arr)/2)
        if len(arr) < 2:
            return arr
        else:
            r = arr[:n]
            l = arr[n:]
            return [func_split(r), func_split(l)]

def func_merge(r, l):
    res = []
    i, j = 0, 0
    while i < len(r) and j < len(l):
        if r[i] < l[j]:
            res.append(r[i])
            i += 1
        else:
            res.append(l[j])
            j += 1
    res += r[i:]
    res += l[j:]
    return res

'''
def func_emerge (arr, r = 0, rig = [], res = []):

    #print(r, l)
    for n, i in enumerate(arr):
        #print(i)
        if isinstance(i, list):
           # print(i)

            if n < 1:
                #print(i)
                if  len(arr[n + 1]) < 2:
                    if r:
                        print(r)
                        res = func_merge(r, func_merge(i, arr[n + 1]))
                        print(res)
                    else:
                        res = [func_merge(i, arr[n + 1])]
                        #print(l)

                else:
                    for j in i:
                        if not isinstance(j, list):
                            r = [j]

            func_emerge(i, r, l, res)
    #print(res)
'''







print(func_split(array))
print('*' * 10)
#print(func_emerge(func_split(array)))



