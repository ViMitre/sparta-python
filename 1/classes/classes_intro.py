class Dog:
    # Initialisation
    def __init__(self, name, color):
        self.animal_type = 'canine'
        self.name = name
        self.color = color
        self.legs = 4
        self.bark()

    def bark(self):
        print(f"Woof! I am {self.name}, a {self.animal_type}")


# print(Dog)
# print(Dog.animal_type)
# print(Dog.bark)

# Instantiation

fido = Dog("Fido", "Black")
lassie = Dog("Lassie", "Brown")

print(fido)
print(type(fido))
print(fido.animal_type)
print(fido.bark())
print(lassie.bark())

fido.animal_type = "arachnid"  # Changes this instance of the class
print(fido.animal_type)
print(lassie.animal_type)

Dog.animal_type = "arachnid"  # Changes all instances of the class

print(fido.animal_type)
print(lassie.animal_type)

print(fido.name)
print(fido.color)
print(lassie.name)
print(lassie.color)

Dog.legs = 8
print(fido.legs)

fido.legs = 3
print(fido.legs)
