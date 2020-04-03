def sum_numbers(numbers):
    return sum (list(map(int, numbers)))


last_sum = 0
while True:

    number = input('Enter space-separated numbers or click Q for exit: ')

    my_numbers = number.split()

    if 'q' in number:
        my_numbers.remove('q')

        print(sum_numbers(my_numbers)+last_sum)
        break
    else:

        last_sum += sum_numbers(my_numbers)
        print(last_sum)








