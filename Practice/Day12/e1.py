
class Apple:
    def __init__(self, w, c, s, f):
        self.weight = w
        self.color = c
        self.size = s
        self.fruit = f
        print("Created!")

    def wpr(self):
        print(self.fruit)

ap1 = Apple(100, "red", "big", "orange")
ap1.wpr()

print(Apple)
