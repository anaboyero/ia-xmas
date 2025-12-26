import unittest
from unittest.mock import MagicMock
from weather_processor import WeatherProcessor

class TestWeatherProcessor(unittest.TestCase):
    def setUp(self):
        # Create a mock WeatherFetcher
        self.mock_fetcher = MagicMock()
        # Import or define WeatherProcessor in your project
        # For this example, let's define a minimal version here
    

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

    def test_high_rain_chance_at_6h(self):
        self.mock_fetcher.get_chance_of_rain.return_value = [0.1, 0.15, 0.85, 0.7, 0.1, 0.05, 0.02, 0.01]
        processor = self.WeatherProcessor(self.mock_fetcher)
        message = processor.get_rain_forecast("Tokyo", hour=6)
        # The expected content should mention "high chance of rain", so this assertion will currently fail
        self.assertIn("high chance of rain", message)

    def test_moderate_rain_chance_at_12h(self):
        self.mock_fetcher.get_chance_of_rain.return_value = [0.05, 0.05, 0.12, 0.85, 0.55, 0.2, 0.1, 0.05]
        processor = self.WeatherProcessor(self.mock_fetcher)
        message = processor.get_rain_forecast("Paris", hour=12)
        # This should eventually mention "moderate chance of rain"
        self.assertIn("moderate chance of rain", message)

    def test_low_rain_chance_at_21h(self):
        self.mock_fetcher.get_chance_of_rain.return_value = [0.05, 0.05, 0.05, 0.12, 0.1, 0.15, 0.2, 0.3]
        processor = self.WeatherProcessor(self.mock_fetcher)
        message = processor.get_rain_forecast("Madrid", hour=21)
        self.assertIn("low chance of rain", message)

    def test_very_low_rain_chance_at_15h(self):
        self.mock_fetcher.get_chance_of_rain.return_value = [0.01, 0.02, 0.03, 0.01, 0.05, 0.12, 0.63, 0.62]
        processor = self.WeatherProcessor(self.mock_fetcher)
        message = processor.get_rain_forecast("Cape Town", hour=15)
        self.assertIn("very low chance of rain", message)

    
# - Use unittest.mock.MagicMock or unittest.mock.patch to replace WeatherFetcher with a mock.
# - Set the return_value of get_current_temperature for different test scenarios.
# - Set the return_value of get_chance_of_rain for rain forecast scenarios.

if __name__ == '__main__':
    unittest.main()
