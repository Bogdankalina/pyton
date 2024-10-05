class  Animals:
    can = "Можуть їсти"



class Birds(Animals):
    height = "Маленькі"
    cani = "Можуть літати"
    sing = "Cпівають"

class Mammals(Animals):
    havelaps = 4
    cam = "Можуть стрибати"

class Tit(Birds):
    def __init__(self):
        print(self.sing)
        print(self.cani)
        print(self.height)

class Sparrow(Birds):
    def __init__(self):
        print(self.sing)
        print(self.cani)
        print(self.height)

class Dog(Mammals):
    def __init__(self):
        print(self.cam)
        print(self.havelaps)

class Cat(Mammals):
    def __init__(self):
        print(self.cam)
        print(self.havelaps)

cat = Cat()
dog = Dog()
sparrow = Sparrow()
tit = Tit()