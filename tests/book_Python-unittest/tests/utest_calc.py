import unittest
import calc


class CalcTests(unittest.TestCase):
    """Info in class."""

    @classmethod
    def setUpClass(cls):
        """Set up for class."""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class."""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for each test."""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for each test."""
        print("Tear down for [" + self.shortDescription() + "]")

    def test_add(self):
        """Info in function."""
        print("Work... id: {}".format(self.id()))
        self.assertEqual(calc.add(1, 2), 3)

    def test_mul(self):
        """Info in second function."""
        print("Work... id: {}".format(self.id()))
        self.assertEqual(calc.mul(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
