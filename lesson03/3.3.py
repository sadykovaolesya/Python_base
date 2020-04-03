
def my_func (num_1, num_2, num_3):

    max_1 = max(num_1, num_2)
    max_2 = max(num_1, num_3)
    max_3 = max(num_2, num_3)
    if max_1 == max_2:
        return max_1 + max_3
    else:
        return max_1 + max_2

print(my_func(4, 5, 3))
