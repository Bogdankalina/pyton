import random

class Student:

    def __init__ (self, name):
        self.name = name
        self.progres = 0
        self.gladness = 50
        self.alive = True
        self.energy = 30

    def to_study(self):
        print("Я навчаюсь")
        self.progres += 1
        self.gladness -= 3
        self.energy -= 2

    def play_game(self):
        print("Я пішов грати")
        self.progres -= 0.1
        self.gladness += 5
        self.energy -= 2

    def go_park(self):
        print("Я пішов в парк")
        self.progres -= 0.1
        self.gladness += 3
        self.energy -= 1

    def to_sleep(self):
        print("Я пішов спати")
        self.progres += 0.1
        self.gladness += 3
        self.energy += 5

    def to_chill(self):
        print("Я відпочиваю")
        self.gladness += 5
        self.progres -= 0.2
        self.energy += 4

    def info(self):
        print(f"Рівень навчання {self.progres}")
        print(f"Рівень задоволення {self.gladness}")
        print(f"Рівень енергії{self.energy}")

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

        if self.energy <= 5:
            print("Я дуже устав")

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
        choice2 = random.randint(1, 20)
        if choice2 == 20:
            self.func()
        self.info()
        self.is_alive()




student = Student("Artem")
for day in range(365):
    if student.alive == False:
        break
    student.live(day)