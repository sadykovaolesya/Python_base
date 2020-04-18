class Cell:
    def __init__(self,count):
        self.count = count
    def __add__(self, other):
        return self.count+other.count

    def __sub__(self, other):
        if self.count-other.count > 0:
            return self.count-other.count
        else:
            return 'Cells are less than zero'

    def __mul__(self, other):
        return self.count*other.count

    def __truediv__(self, other):
        return int(self.count/other.count)

    def make_order(self,n):
        cell = ''
        for i in range(1,self.count+1):
            cell +='*'
            if i%n == 0:
                cell +='\n'
        print(cell)


cell1 = Cell(12)
cell2 = Cell(6)
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
cell1.make_order(5)
