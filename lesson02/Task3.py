x = int(input('Введите число: '))

def join_numbers(num1, num2):
    return num1*10+num2

def get_number(a, num = 0):
    if a % 10 == a:
        return join_numbers(num, a)
    else:
        return get_number(int(a / 10),join_numbers(num, (a % 10)))

result = get_number(x)

print(result)