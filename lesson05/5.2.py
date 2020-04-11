with open('myfile.txt') as f:
    count = 0
    for line in f:
        count +=1
        print(f' Word conut in line {count} - {len(line.split())}')
    print(f'Number of lines - {count}')

