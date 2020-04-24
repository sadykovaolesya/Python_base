from abc import ABC, abstractmethod

class Close:
    @abstractmethod
    def expence(self,x):
        pass

class Suit(Close):
    def expense (self,v):
        self.ex = 2*v+0.3
        return self.ex


class Coat(Close):
    def expense (self,h):
        self.ex =  h/6.5+0.5
        return self.ex


coat = Coat()
print(coat.expense(3))

suit = Suit()
print(suit.expense(2))

