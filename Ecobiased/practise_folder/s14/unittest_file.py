import unittest


def add_number(a, b):
    return a + b


class TestAdditionNumber(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(add_number(2, 3), 5)

    def test_negative_number(self):
        self.assertEqual(add_number(-2, -3), -5)

    def test_mixed_number(self):
        self.assertEqual(add_number(-3, 5), 2)



# unittest for class



class Calculator:

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("cannot divide by 0.")
        return a/b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)


if __name__=='__main__':
    unittest.main()