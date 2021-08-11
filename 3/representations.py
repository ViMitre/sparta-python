class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"

bham_academy = Location(52.488647, -1.887249)
print(bham_academy)
print(bham_academy.__repr__())
print(bham_academy.__str__())
print(repr(bham_academy))


print(f"The Birmingham Academi is located at: {bham_academy}")



# n = 0.003453
# print(f"Fixed point: {n:f}")
# print(f"Exponential notation: {n:e}")


class Cat:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old cat"

    def __format__(self, format_spec):
        if format_spec == 'dog':
            return f"A {self.age*7} dog-years old cat"
        elif format_spec == 'cat':
            return f"A {self.age*5} cat-years old cat"
        else:
            return self.__str__()

whiskers = Cat(6)


print(f"whiskers is {whiskers}")
print(f"whiskers is {whiskers:dog}")
print(f"whiskers is {whiskers:cat}")
