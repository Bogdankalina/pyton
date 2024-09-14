class Student:

    count_of_student = 1
    def __init__(self, name, age=5):
        self.age = age
        self.name = name
    def info(self):
        print(f"Я {self.name},мені {self.age} років(роки)")

    def info1(self):
        print(f"Я в сім'ї {self.count_of_student} пес")

    def info2(self):
        print(f"Я люблю грати в CS 2")

    def info2(self):
        print(f"Я це мій друг Barbos")





Barbos = Student(name="Barbos")
Bobik = Student(name= "Bobik" ,age=4)

Barbos.info()
Barbos.info1()
Barbos.info2()
Bobik.info()
Bobik.info2()







