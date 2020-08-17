#https://drive.google.com/file/d/1201zYup7cMxCdk_UJHVaooTVBC1LZ9jA/view?usp=sharing

def sum_numbers(num1, num2):
    return num1 + num2

def mul_numbers(num1, num2):
    return num1 * num2

def sub_numbers(num1, num2):
    return num1 - num2

def div_numbers(num1, num2):
    return num1 / num2

while True:
    a = float(input('ВВедите первое число: '))
    b = float(input('ВВедите второе число: '))
    operate = input('ВВедите знак операции: ')
    if operate == '0':
        break
    elif operate == '+':
        print(sum_numbers(a, b))
    elif operate == '*':
        print(mul_numbers(a, b))
    elif operate == '-':
        print(sub_numbers(a, b))
    elif operate == '/':
        if b != 0:
            print(div_numbers(a, b))
        else:
            print("Деление на 0")
    else:
        print("Неверный знак операции")
