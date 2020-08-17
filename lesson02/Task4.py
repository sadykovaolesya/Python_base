n = int(input('Введите количество элементов: '))

def get_sum_numbers(n, a=1, total=0):
    if n == 1:
        return total + a
    else:
        return get_sum_numbers(n - 1, -a / 2, total + a)

result = get_sum_numbers(n)

print(result)
