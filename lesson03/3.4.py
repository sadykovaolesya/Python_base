def my_func (x,y):
    print  (x**y)

    i = 1
    xr = x
    while i < abs(y):
        x = xr * x
        i +=1
    print(1/x)

my_func(4, -2)