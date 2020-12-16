class Horse():
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

class Rider():
    def __init__(self,name):
        self.name = name

mich = Rider("michael")
wa = Horse("wawa",mich)

print(wa.owner.name)
