n = int (input('Enter number: '))

max = 0
while n > 0:
    a = int(n % 10)
    n = int(n / 10)

    if a > max:
        max = a


print(max)

