import unittest
from bot import calculate_factorial

class TestBot(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(calculate_factorial(0), 1)
    
    def test_factorial_positive(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(3), 6)

if __name__ == '__main__':
    unittest.main()