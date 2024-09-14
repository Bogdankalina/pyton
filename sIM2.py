import random

class Student:

    def __init__ (self, name):
        self.name = name
        self.progres = 0
        self.gladness = 50
        self.alive = True

    def to_study(self):
        print("Я навчаюсь")
        self.progres += 0.1
        self.gladness -= 3

    def to_sleep(self):
        print("Я пішов спати")
        self.progres += 0.02
        self.gladness += 3

    def to_chill(self):
        print("Я відпочиваю")
        self.gladness += 5
        self.progres -= 0.1

    def info(self):
        print(f"Рівень навчання {self.progres}")
        print(f"Рівень задоволення {self.gladness}")


    def is_alive(self):
        if self.progres > 10:
            print("Ми все вивчили і закінчилм МКА ШАГ")
            self.alive = False
        if self.progres < -0.5:
            print("Ми втратили інтерес до навчання,,,,")
            self.alive = False
        if self.gladness <= 0:
            print("У мене депресія")
            self.alive = False


    def live(self, day):
        print(f"День{day} з життя {self.name}")
        print("======================================")
        choice = random.randint(1,3)
        if choice == 1:
            self.to_study()
        elif choice == 2:
            self.to_sleep()
        elif choice == 3:
            self.to_chill()
        self.info()
        self.alive()




student = Student("Artem")
for day in range(365):
    if student.alive == False:
        break
    student.live(day)