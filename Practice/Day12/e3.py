class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.hight = h

    def area(self):
        return self.base*self.hight/2

tr1 = Triangle(2, 5)
ar1 = tr1.area()

print(ar1)
