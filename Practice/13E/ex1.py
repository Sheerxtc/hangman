class Rectangle:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    def calculate_perimeter(self):
        return self.l1+self.l2+self.l3     



class Square:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def calculate_perimeter(self):
        return 2*(self.l1+self.l2)

r = Rectangle(1, 2, 3)
s = Square(5, 2)

print(r.calculate_perimeter())
print(s.calculate_perimeter())
