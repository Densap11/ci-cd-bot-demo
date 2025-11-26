
import unittest
from bot import calculate_factorial

class TestFactorialBot(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(calculate_factorial(0), 999)  #Ошибка
    
    def test_factorial_positive_numbers(self):
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(3), 6)
    
    def test_factorial_medium_number(self):
        self.assertEqual(calculate_factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()