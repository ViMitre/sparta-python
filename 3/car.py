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
        if self.current_speed > self.max_speed:
            return self.max_speed
        elif self.current_speed < 0:
            return 0
        else:
            return self.current_speed

    def accelerate(self, speed):
        self.current_speed += speed

    def decelerate(self, speed):
        self.current_speed -= speed


my_car = Car(60, 200)
my_car.accelerate(20)

print(my_car.get_speed())

my_car.decelerate(120)

print(my_car.get_speed())

my_car.accelerate(400)
print(my_car.get_speed())
