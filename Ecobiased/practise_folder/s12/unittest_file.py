import unittest


def add_number(a, b):
    return a + b


class TestAdditionNumber(unittest.TestCase):

    def test_positive_number(self):
        self.assertEqual(add_number(2, 3), 5)

    def test_negative_number(self):
        self.assertEqual(add_number(-2, -3), -5)

    def test_mixed_number(self):
        self.assertEqual(add_number(-3, 4), 1)


if __name__=='__main__':
    unittest.main()
