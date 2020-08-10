a = float(input('ВВедите первое число: '))
b = float(input('ВВедите первое число: '))
c = float(input('ВВедите первое число: '))

if  a > b and a > c:
    if b > c:
        print(f'avar = {b}')
    else:
        print(f'avar = {c}')
else:
    if b > a and b > c:
        if a > c:
            print(f'avar = {a}')
        else:
            print(f'avar = {c}')
    else:
        if a > b:
            print(f'avar = {a}')
        else:
            print(f'avar = {b}')
