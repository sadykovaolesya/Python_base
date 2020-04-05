from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

i = 0
for el in cycle('34'):
    if i > 3:
        break
    print(el)
    i += 1

