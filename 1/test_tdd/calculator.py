import math


class SimpleCalculator():

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2


class SciCalculator(SimpleCalculator):
    def sqrt(self, num):
        return math.sqrt(num)

    def floor(self, num):
        return math.floor(num)

    def ceil(self, num):
        return math.ceil(num)
