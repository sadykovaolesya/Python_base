from functools import reduce

def my_func (el1, el2):
    return el1*el2

my_list = [number for number in range(100, 1001) if number%2 == 0]

print(reduce(my_func, my_list))





