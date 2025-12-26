import unittest

def is_strong_password(pwd):
    return False  # minimal implementation so tests compile

class TestIsStrongPassword(unittest.TestCase):
    def test_short_password(self):
        self.assertFalse(is_strong_password("A1@b"))  # Too short

    def test_no_uppercase(self):
        self.assertFalse(is_strong_password("abc1@def"))  # No uppercase letter

    def test_no_lowercase(self):
        self.assertFalse(is_strong_password("ABC123@#"))  # No lowercase letter

    def test_no_digit(self):
        self.assertFalse(is_strong_password("Abcdef@#"))  # No digit

    def test_no_special_character(self):
        self.assertFalse(is_strong_password("Abcdef12"))  # No special char

    def test_strong_password(self):
        self.assertTrue(is_strong_password("Abcdef1@"))  # Meets all criteria

if __name__ == '__main__':
    unittest.main()
