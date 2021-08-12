# Four pillars

# Abstraction - use methods to make life easier
# Encapsulation - hide away dangerous things
# Inheritance -
# Polymorphism

class Animal:
    def __init__(self):
        self.alive = True

    def hunt(self):
        print("Searching for food")

    def move(self):
        print("Moving")


class Reptile(Animal):
    def __init__(self, reptile_type):
        super().__init__()
        self.reptile_type = reptile_type


class Snake(Reptile):
    def __init__(self):
        super().__init__("Snake")


class Mammal(Animal):
    def __init__(self):
        super().__init__()

    def breed(self):
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self):
        super().__init__()

    def breed(self):
        print("Laying eggs")


r = Reptile("snake")
r.hunt()
r.move()
print(r.reptile_type)

s = Snake()
print(s.reptile_type)

perry = Platypus()
perry.breed()

m = Mammal()
m.breed()


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


rect = Rectangle(23, 43)
print(rect.area())

sq = Square(5)
print(sq.area())
