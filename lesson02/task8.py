num = int(input('Введите число: '))
numbers = int(input('Введите последовательность чисел: '))


def get_count_number(n, num_list, count=0):
    if num_list % 10 == num_list:
        if num_list == n:
            return count + 1
        else:
            return count
    else:
        if num_list % 10 == n:
            return get_count_number(n, int(num_list / 10), count + 1)
        else:
            return get_count_number(n, int(num_list / 10), count)


result = get_count_number(num, numbers)
print(result)
