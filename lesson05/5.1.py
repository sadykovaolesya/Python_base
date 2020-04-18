out_f = open ('my_file.txt', 'w')
while True:
    my_text = input('Enter text: ')
    if my_text:
        out_f.write(my_text +'\n')
    else:
        out_f.close()
        break

