import unittest
import funcs


@unittest.skip("No need")
class ClearAndReverseTest(unittest.TestCase):
    def test_string_two_words(self):
        self.assertEqual(funcs.clear_and_reverse("Hello world!"), "!dlrowolleH")


if __name__ == '__main__':
    unittest.main()
