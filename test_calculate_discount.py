import unittest
from calculate_discount import calculate_discount

class TestCalculateDiscount(unittest.TestCase):
    def test_regular_discount(self):
        result = calculate_discount(100, "regular")
        self.assertEqual(result, 95)

    def test_premium_discount(self):
        result = calculate_discount(200, "premium")
        self.assertEqual(result, 180)

    def test_vip_discount(self):
        result = calculate_discount(400, "vip")
        self.assertEqual(result, 300)

    def test_zero_price(self):
        result = calculate_discount(0, "regular")
        self.assertEqual(result, 0)

    def test_invalid_user_type(self):
        with self.assertRaises(Exception):
            calculate_discount(100, "guest")


if __name__ == '__main__':
    unittest.main()
