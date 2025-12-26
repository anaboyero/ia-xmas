import unittest
from unittest.mock import MagicMock

class TestWeatherProcessor(unittest.TestCase):
    def setUp(self):
        # Create a mock WeatherFetcher
        self.mock_fetcher = MagicMock()
        # Import or define WeatherProcessor in your project
        # For this example, let's define a minimal version here
        class WeatherProcessor:
            def __init__(self, fetcher):
                self.fetcher = fetcher
            def get_city_temperature_info(self, city):
                temp = self.fetcher.get_current_temperature(city)
                if temp is None:
                    return f"Temperature data for {city} not available."
                if temp < 0:
                    return f"It's freezing in {city}: {temp}°C"
                elif temp > 30:
                    return f"It's hot in {city}: {temp}°C"
                else:
                    return f"The temperature in {city} is {temp}°C"

        self.WeatherProcessor = WeatherProcessor

    def test_freezing_temperature(self):
        self.mock_fetcher.get_current_temperature.return_value = -5
        processor = self.WeatherProcessor(self.mock_fetcher)
        info = processor.get_city_temperature_info("Oslo")
        self.assertIn("freezing", info)
        self.assertIn("-5°C", info)

    def test_hot_temperature(self):
        self.mock_fetcher.get_current_temperature.return_value = 35
        processor = self.WeatherProcessor(self.mock_fetcher)
        info = processor.get_city_temperature_info("Dubai")
        self.assertIn("hot", info)
        self.assertIn("35°C", info)

    def test_moderate_temperature(self):
        self.mock_fetcher.get_current_temperature.return_value = 20
        processor = self.WeatherProcessor(self.mock_fetcher)
        info = processor.get_city_temperature_info("London")
        self.assertIn("20°C", info)
        self.assertTrue(info.startswith("The temperature in London is"))

    def test_temperature_not_available(self):
        self.mock_fetcher.get_current_temperature.return_value = None
        processor = self.WeatherProcessor(self.mock_fetcher)
        info = processor.get_city_temperature_info("Atlantis")
        self.assertIn("not available", info)

# This is how you can mock WeatherFetcher in your WeatherProcessor tests:
# - Use unittest.mock.MagicMock or unittest.mock.patch to replace WeatherFetcher with a mock.
# - Set the return_value of get_current_temperature for different test scenarios.

if __name__ == '__main__':
    unittest.main()
