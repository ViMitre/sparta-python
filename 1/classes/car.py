# Max speed

# Current speed
# Getter - return current speed
# Accelerate and decelerate methods

# Accelerate past max speed
# What if it keeps braking?

class Car:
    def __init__(self, current_speed, max_speed):
        self.current_speed = current_speed
        self.max_speed = max_speed

    def get_speed(self):
        return self.current_speed

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        self.current_speed = min(self.max_speed, new_speed)

    def decelerate(self, brake):
        new_speed = self.current_speed - brake
        self.current_speed = max(0, new_speed)


my_car = Car(60, 200)
my_car.accelerate(20)

print(my_car.get_speed())

my_car.decelerate(120)

print(my_car.get_speed())

my_car.accelerate(400)
print(my_car.get_speed())
