my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [number for number in my_list[1:] if  number > my_list[my_list.index(number)-1]]


print(result)