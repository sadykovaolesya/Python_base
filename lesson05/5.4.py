my_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open ('my_file_4_1.txt') as f:
    out_f = open('my_file_4_2.txt', 'w')
    for line in f:
        content = line.split('—')
        out_f.write(my_dict[content[0]] +'—'+ content[1])

    out_f.close()