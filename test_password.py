import unittest
from password import is_strong_password
class TestIsStrongPassword(unittest.TestCase):
    def test_short_password(self):
        result = is_strong_password("A1@b")
        self.assertIsInstance(result, list)
        self.assertIn("Password is too short. You need at least 8 characters", result)

    def test_no_uppercase(self):
        result = is_strong_password("abc1@def")
        self.assertIsInstance(result, list)
        self.assertIn("Password does not contain an uppercase letter", result)

    def test_no_lowercase(self):
        result = is_strong_password("ABC123@#")
        self.assertIsInstance(result, list)
        self.assertIn("Password does not contain a lowercase letter", result)

    def test_no_digit(self):
        result = is_strong_password("Abcdef@#")
        self.assertIsInstance(result, list)
        self.assertIn("Password does not contain a digit", result)

    def test_no_special_character(self):
        result = is_strong_password("Abcdef12")
        self.assertIsInstance(result, list)
        self.assertIn("Password does not contain a special character. You need to use at least one of the following characters: @#_!-?$%&()[]{}", result)

    def test_strong_password(self):
        result = is_strong_password("Abcdef1@")
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
