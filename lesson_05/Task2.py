from collections import deque
alf = { 0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
}

def get_val(val):
    for key, value in alf.items():
        if val == key:
            return value

def get_key(k):
    for key, value in alf.items():
        if k == value:
            return key


num1 = deque(input('ВВедите первое число в 16-ой системе счисления: '))
num2 = deque(input('ВВедите второе число в 16-ой системе счисления: '))
print(f'Первое число {num1}')
print(f'Второе число {num2}')
if len(num1) > len(num2):
    for _ in range(len(num1) - len(num2)):
        num2.appendleft('0')
else:
    for _ in range(len(num2) - len(num1)):
        num1.appendleft('0')
num1.reverse()
num2.reverse()
d = deque()
count = 0
for i in range (len(num1)):
    a = get_key(num1[i])
    b = get_key(num2[i])
    if count > 0:
        res = a + b + count
        count = 0
    else:
        res = a + b
    if res > 9 and res < 16:
        d.appendleft(get_val(res))
    elif res >= 16:
        d.appendleft(get_val(res - 16))
        count +=1
    else:
        d.appendleft(res)
if count > 0:
    d.appendleft(count)
print(f'Сумма чисел {d}')

