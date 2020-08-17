x = int(input('Введите число: '))

def get_count_even_uneven(a, even = 0, uneven = 0):
    if a % 10 == a:
        if a % 2 == 0:
            return f'Четных чисел - {even + 1 }, нечетных чисел - {uneven}'
        else:
            return f'Четных чисел - {even}, нечетных чисел - {uneven + 1}'
    else:
        if a % 10 % 2 == 0:
            return get_count_even_uneven(int(a / 10),even + 1, uneven)
        else:
            return get_count_even_uneven(int(a / 10), even, uneven + 1)

print(get_count_even_uneven(x))





