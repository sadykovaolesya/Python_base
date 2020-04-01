my_list =  [7, 5, 3, 3, 2]

number = int (input('Enter a number'))

for el in my_list:

    if number > el:
        if number > max(my_list):
            my_list.insert(0, number)
            break
        else:
            pos = my_list.index(el)
            my_list.insert(pos, number)
            break

    elif number < el and (len(my_list)-1) == my_list.index(el):
         pos = my_list.index(el)
         my_list.insert(pos+1, number)

print(my_list)