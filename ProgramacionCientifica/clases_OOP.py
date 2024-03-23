# Sobre OOP, ejemplo calse animal

class Animal():
    def __init__(self, value):
        self.species = value

    def eat(self, food):
        print(f"The animal is eating {food}")

hummingbird = Animal('Bird')
hummingbird.eat('Nectar')
print(f"The object belongs to the species {hummingbird.species}")