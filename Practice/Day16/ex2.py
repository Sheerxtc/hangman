class Square():
    def __init__(self, l):
        self.len = l

    def __repr__(self):
          return """{} by {} by {} by {}""".format(self.len,
                                    self.len,
                                    self.len,
                                    self.len)
    
s1 = Square(29)
print(s1)
