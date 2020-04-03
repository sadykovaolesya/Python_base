text = input('Enter string with a space: ').split()

for ind, el in enumerate(text, 1):
    print( ind, el if len(el) < 10 else el [:10])

 