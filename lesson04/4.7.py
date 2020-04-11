def fact(number):
    for el in range (1,number+1):
        yield el

res = 1
for el in fact(5):
    res *= el
    print(res)


