class Square:
    def __init__(self, l, change_len):
        self.l = l
        self.change_len = change_len

    def change_size(self):
        self.change_len = int(input("Tpye a change size:"))
        return self.l+self.change_len

s1 = Square(15, 0)
print(s1.change_size())

