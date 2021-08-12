from calculator import SimpleCalculator
import unittest

class CalculatorTests(unittest.TestCase):
    calc = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 7), 9)
        self.assertEqual(self.calc.add(-5, -20), -25)

    def test_sub(self):
        self.assertEqual(self.calc.sub(30, 3), 27)
        self.assertEqual(self.calc.sub(-5, -2), -3)

    def test_mult(self):
        self.assertEqual(self.calc.mult(2, 6), 12)
        self.assertEqual(self.calc.mult(-5, -4), 20)

    def test_div(self):
        self.assertEqual(self.calc.div(9, 3), 3)
        self.assertEqual(self.calc.div(-6, -3), 2)