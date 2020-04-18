with open('my_file.txt') as f:
    count = 0
    salary = 0
    for line in f:
        content = line.split()
        if float(content[1]) < 20000:
            print(content[0])
        salary += float (content [1])
        count += 1
    print(salary/count)




