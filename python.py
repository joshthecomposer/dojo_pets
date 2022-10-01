import pet
import random as rd

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        random_food = rd.randint(0, len(self.pet_food) - 1)
        print(f"You fed {self.pet.name} some {self.pet_food[random_food]}")
        return self

    def bathe(self):
        self.pet.noise()
        return self


josh_treats = ["milkbones", "scooby snacks"]
josh_food = ["hill's science diet", "canned food"]
ike_tricks = ["jump", "speak", "dance"]

ike = pet.Dog("Ike", ike_tricks)

josh = Ninja("Joshua", "Wise", ike, josh_treats, josh_food)

josh.walk().bathe().feed()