import random as rd

class Pet:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks
        self.energy = 0
        self.health = 0

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        random_trick = rd.randint(0, len(self.tricks) - 1)
        print(f"You go on a walk, {self.name} decides to {self.tricks[random_trick]}")
        return self

    def noise(self):
        print(f"{self.name} does a loud {self.sound}!")
        return self

class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks)
        self.sound = "Bark"

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks)
        self.sound = "Meow"
        tricks = tricks.append("Rub against your leg")

class Bird(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, tricks)
        self.sound = "Chirp"
        tricks = tricks.append("Fly")