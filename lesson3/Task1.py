START_i = 2
STOP_i = 99
START_j = 2
STOP_j = 9

for j in range (START_j, STOP_j + 1):
    count = 0
    for i in range (START_i, STOP_i + 1):
        if i % j == 0:
            count += 1
    print(f'{j} - кратно {count} раз')



