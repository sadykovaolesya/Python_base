my_dict = {}

with open('my_file_6.txt') as f:
    for line in f:
        content = line.split()
        sum_num = 0
        for el in content[1:]:
            num = el[:el.find('(')]
            if num:
                sum_num += int(num)
       
        my_dict[content[0]] = sum_num

    print(my_dict)