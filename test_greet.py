import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet(self):
        NAME = "Carlos"
        self.assertEqual(greet(NAME), f"Hello {NAME}!")

    def test_greet_empty_string(self):
        self.assertEqual(greet(""), "Hello !")

    def test_greet_none(self):
        self.assertEqual(greet(None), "Hello!")

if __name__ == '__main__':
    unittest.main()



