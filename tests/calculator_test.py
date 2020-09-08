import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    def test_multiply(self):
        self.assertEqual(6, multiply(3,2))

    def test_divide(self):
        self.assertEquals(3, divide(27,9))