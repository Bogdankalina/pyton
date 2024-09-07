class Student:
    count_of_student = 0
    def __init__(self, name, age=15):
        self.age = age
        self.name = name
        print("Hi")
        Student.count_of_student += 1
    #def info(self):
     #   print(f"Я{self.name},мені {self.age} років")

    def __del__(self):
        print(f"я {self.name}, і я пішов")

    def __len__(self):
        return self.age

    def grow(self, delta=1):
        oldAge = self.age
        self.age += delta
        if self.age > 100:
            print("Error Age")
            return
        self.age = oldAge




        print(Student.count_of_student)


Anton = Student(name="Anton")
print(Anton.age)
Anton.grow()
Kirill = Student(name="Kirill", age=17)
print(Kirill.age)

print(Student.count_of_student)

Anton.info()
Kirill.info()

print(len(Anton))