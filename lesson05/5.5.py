with open('my_file_5.txt','w') as f:
    number = input('Enter space-separated numbers: ')
    print(number, file=f)

with open('my_file_5.txt','r') as f:
    numbers = sum(map (int, f.read().split()))
    print(numbers)
