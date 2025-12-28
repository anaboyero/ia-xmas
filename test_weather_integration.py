import unittest

from weather_fetcher import WeatherFetcher
from weather_processor import WeatherProcessor



class TestWeatherIntegration(unittest.TestCase):

    def setUp(self):
        self.fetcher = WeatherFetcher()
        self.processor = WeatherProcessor(self.fetcher)

    def test_city_temperature_info_integration(self):
        # This tests that WeatherProcessor fetches temperature info correctly from WeatherFetcher and formats output.
        result = self.processor.get_city_temperature_info("London")
        # Should be an integer in test_fetcher (20) and processor formats as "The temperature in LONDON is 20°C"
        self.assertIn("20°C", result)
        self.assertTrue(result.startswith("The temperature in London is") or result.startswith("The temperature in London is"))

    def test_city_temperature_info_integration_freezing(self):
        result = self.processor.get_city_temperature_info("OSLO")
        self.assertIn("-5°C", result)
        # could be "It's freezing in Oslo: -5°C" or similar
        self.assertTrue("freezing" in result or "Freezing" in result)

    def test_city_temperature_info_city_not_found(self):
        with self.assertRaises(Exception):
            # WeatherFetcher raises on bad city
            self.processor.get_city_temperature_info("Atlantis")

    def test_rain_forecast_integration(self):
        # For LONDON, rain probs: [0.1, 0.2, 0.15, 0.25, 0.05, 0.12, 0.33, 0.41], see fetcher
        # Our time slots: [0, 3, 6, 9, 12, 15, 18, 21]
        # Let's use hour=6, maps to index 2, value 0.15 --> 'very low' or 'low' (depending on thresholds)
        forecast = self.processor.get_rain_forecast("London", 6)
        self.assertIn("London", forecast)
        self.assertTrue("chance of rain" in forecast)
        # 0.15 is below LOW_RAIN_PROBABILITY=0.2, so should be 'very low chance of rain'
        self.assertIn("very low chance of rain", forecast)

    def test_rain_forecast_integration_moderate(self):
        # hour=18 is index 6: 0.33 (should be 'low' as 0.33 >= 0.2 but < 0.5)
        forecast = self.processor.get_rain_forecast("London", 18)
        self.assertIn("low chance of rain", forecast)

    def test_rain_forecast_city_unknown(self):
        with self.assertRaises(Exception):
            self.processor.get_rain_forecast("Atlantis", 12)

    def test_rain_forecast_invalid_hour(self):
        with self.assertRaises(ValueError):
            self.processor.get_rain_forecast("London", 24)

    def test_rain_forecast_invalid_city_type(self):
        with self.assertRaises(TypeError):
            self.processor.get_rain_forecast(123, 6)

if __name__ == "__main__":
    unittest.main()
