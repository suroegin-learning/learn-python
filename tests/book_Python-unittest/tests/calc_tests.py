import unittest
import calc


class CalcTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(2, 2), 4)

    @unittest.skip("Temporary ignoring...")
    def test_sub(self):
        self.assertEqual(calc.sub(5, 1), 4)


@unittest.skip("TEMP DECIDE")
class CalcExTests(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(calc.sqrt(4), 2)

    def test_pow(self):
        self.assertEqual(calc.pow(3, 3), 27)
