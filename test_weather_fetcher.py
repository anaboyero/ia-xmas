import unittest

class TestWeatherFetcher(unittest.TestCase):
    def setUp(self):
        # We're not implementing the real WeatherFetcher, so this will fail
        from weather_fetcher import WeatherFetcher
        self.fetcher = WeatherFetcher()

    def test_get_chance_of_rain_returns_list_of_probabilities(self):
        # We expect a list with 8 float values between 0 and 1 for a known city
        result = self.fetcher.get_chance_of_rain("LONDON")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 8)
        for prob in result:
            self.assertIsInstance(prob, (float, int))
            self.assertGreaterEqual(prob, 0)
            self.assertLessEqual(prob, 1)

    def test_get_chance_of_rain_empty_city(self):
        # Should raise an exception for invalid city input
        with self.assertRaises(Exception):
            self.fetcher.get_chance_of_rain("")
    
    def test_get_chance_of_rain_invalid_city(self):
        # Should raise an exception for invalid city input
        with self.assertRaises(Exception):
            self.fetcher.get_chance_of_rain("Atlantis")

    def test_get_city_temperature_info_returns_number(self):
        # The method should return a float or int for a valid city
        temp = self.fetcher.get_city_temperature_info("Oslo")
        self.assertIsInstance(temp, (int, float))

    def test_get_city_temperature_info_city_not_found(self):
        # Should raise an exception or return None for unknown city
        with self.assertRaises(Exception):
            self.fetcher.get_city_temperature_info("Atlantis")

if __name__ == "__main__":
    unittest.main()
