a = int (input('Enter number 1:'))
b = int (input('Enter numbe 2'))

def divide_num (num_1, num_2):

    try:
        return (num_1/num_2)
    except ZeroDivisionError:
        return ('Division by zero')

print (divide_num(a,b))