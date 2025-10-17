import unittest


def add_number(a, b):
    return a+b


class TestAdditionNumber(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(add_number(2, 4), 6)

    def test_negative_number(self):
        self.assertEqual(add_number(-2, -3), -5)

    def test_mixed_number(self):
        self.assertEqual(add_number(-3, 4), 1)


# if __name__=='__main__':
#     unittest.main()


class Calculator:

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can not divide by zero")
        return a/b


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(4, 0)


# if __name__ == '__main__':
#     unittest.main()


class Calculator1(unittest.TestCase):

    def multiply1(self, a, b):
        return a * b

    def divide1(self, a, b):
        if b == 0:
            raise ValueError("Can not divide by zero")
        return a/b


class TestCalculator1(unittest.TestCase):

    def setUp(self):
        self.calc1 = Calculator1()

    def test_multiply1(self):
        self.assertEqual(self.calc1.multiply1(2, 4), 8)

    def test_divide1(self):
        self.assertEqual(self.calc1.divide1(4, 2), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc1.divide1(4, 0)

if __name__ == '__main__':
    unittest.main()