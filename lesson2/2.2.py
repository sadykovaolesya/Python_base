my_list = input('Enter numbers with a comma: ').split(',')

print(my_list)
result_list = []

for el in my_list:
    pos = my_list.index(el)
    result_list.insert(pos - 1, el) if pos %2 else  result_list.insert(pos + 1, el)

print(result_list)

