import unittest

class TestWeatherFetcherAttributeUpdates(unittest.TestCase):
    def setUp(self):
        from weather_fetcher import WeatherFetcher
        self.fetcher = WeatherFetcher()

    def test_update_temperatures_and_rain_probabilities_for_new_city(self):
        # Simulate adding/updating methods
        # Add temperature for Berlin and rain probabilities for Berlin
        self.fetcher.temperatures["berlin"] = 13
        self.fetcher.rain_probabilities["berlin"] = [0.11, 0.09, 0.2, 0.4, 0.18, 0.13, 0.09, 0.04]

        # Now they should be available
        temp = self.fetcher.get_city_temperature_info("Berlin")
        self.assertEqual(temp, 13)
        rain_probs = self.fetcher.get_chance_of_rain("Berlin")
        self.assertEqual(rain_probs, [0.11, 0.09, 0.2, 0.4, 0.18, 0.13, 0.09, 0.04])

    def test_overwrite_temperatures_in_existing_city(self):
        # Overwrite Oslo's temperature
        old_oslo_temperature = self.fetcher.get_city_temperature_info("Oslo")
        self.fetcher.temperatures["oslo"] = -1
        new_temp = self.fetcher.get_city_temperature_info("Oslo")
        self.assertEqual(new_temp, -1)
        self.assertNotEqual(new_temp, old_oslo_temperature)

    def test_overwrite_temperature_in_existing_city(self):
        # Overwrite London's rain probabilities
        new_probs = [0.5, 0.3, 0.25, 0.6, 0.7, 0.75, 0.42, 0.54]
        self.fetcher.rain_probabilities["london"] = new_probs
        out_probs = self.fetcher.get_chance_of_rain("London")
        self.assertEqual(out_probs, new_probs)



class TestWeatherFetcher(unittest.TestCase):
    def setUp(self):
        # We're not implementing the real WeatherFetcher, so this will fail
        from weather_fetcher import WeatherFetcher
        self.fetcher = WeatherFetcher()

    def test_get_chance_of_rain_returns_list_of_probabilities(self):
        # We expect a list with 8 float values between 0 and 1 for a known city
        result = self.fetcher.get_chance_of_rain("London")
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 8)
        for prob in result:
            self.assertIsInstance(prob, (float, int))
            self.assertGreaterEqual(prob, 0)
            self.assertLessEqual(prob, 1)

    def test_raise_exception_when_asking_for_chance_of_rain_with_unknown_city(self):
        # Should raise an exception for an unknown city input
        with self.assertRaises(Exception):
            self.fetcher.get_chance_of_rain("Atlantis")

    def test_raise_exception_when_asking_for_city_temperature_info_with_unknown_city(self):
        # Should raise an exception for an unknown city when fetching temperature info
        with self.assertRaises(Exception):
            self.fetcher.get_city_temperature_info("Atlantis")

    def test_raise_exception_when_asking_for_chance_of_rain_with_empty_city(self):
        # Should raise an exception for invalid city input
        with self.assertRaises(Exception):
            self.fetcher.get_chance_of_rain("")

    def test_get_city_temperature_info_returns_number(self):
        # The method should return a float or int for a valid city
        temp = self.fetcher.get_city_temperature_info("Oslo")
        self.assertIsInstance(temp, (int, float))



if __name__ == "__main__":
    unittest.main()
