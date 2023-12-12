import unittest


def add_number(a, b):
    return a + b


class TestAddition(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_number(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_number(-3, -5), -8)

    def test_add_mixed_numbers(self):
        self.assertEqual(add_number(-4, 3), -1)


if __name__ == '__main__':
    unittest.main()
