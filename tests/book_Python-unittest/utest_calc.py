import unittest
import calc


class CalcTest(unittest.TestCase):
    """Info in class."""

    def test_add(self):
        """Info in function."""
        self.assertEqual(calc.add(1, 2), 3)

    def test_mul(self):
        """Info in second function."""
        self.assertEqual(calc.mul(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
