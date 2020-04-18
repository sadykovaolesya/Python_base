class Matrix:
    def __init__(self):

        self.numbers = [[]]

    def __str__(self):
        string = ''
        for i in self.numbers:
            for j in i:
                string += str(j)+ ' '
            string +='\n'
        return string

    def __add__(self, other):
        self.list = []
        self.new_m = []
        if len(self.numbers) == len(other.numbers):
            i = 0
            while i < len(self.numbers):
                self.list = list(map(lambda x,y: x+y, self.numbers[i], other.numbers[i]))
                i +=1
                self.new_m.append(self.list)
        return self.new_m


matrix1 = Matrix ()
matrix1.numbers = [[2, 4], [3, 6], [5, 7]]
print(matrix1)


matrix2 = Matrix()
matrix2.numbers = [[1, 4], [3, 7], [2, 1]]
print(matrix2)

print(matrix1+matrix2)


