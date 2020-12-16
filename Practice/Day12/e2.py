import math
class Circle:
    def __init__(self, r):
        self.radio = r
        
    def area(self):
        return math.pi*self.radio*self.radio
    
r1 = Circle(5)

print(r1)
print(math.pi)

c1 = r1.area()

print(c1)
