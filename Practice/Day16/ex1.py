class Square():
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append((4*l))

s1 = Square(4)
s2 = Square(3)
s3 = Square(1)

print(Square.square_list)
        
