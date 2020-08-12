#https://drive.google.com/file/d/1-yIbUy_deBuhyIbsHGXfkaiah93eXCAo/view?usp=sharing

x = int(input('Введите трехзначное число: '))

a = x // 100
b = (x // 10) % 10
c = x % 10

sum = a + b + c
mult = a * b * c

print(f'Cумма цифр трехзначного числа: {sum}')
print(f'Произведение цифр трехзначного числа: {mult}')
