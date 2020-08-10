x1 = int(input('ВВедите координату x1: '))
y1 = int(input('ВВедите координату y1: '))
x2 = int(input('ВВедите координату x2: '))
y2 = int(input('ВВедите координату y2: '))

k = (y1 - y2) / (x1 - x2)
b = x1 * k - y1
print(f'y = {k}x + {b}')