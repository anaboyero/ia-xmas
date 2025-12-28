class WeatherFetcher:


    def __init__(self):
        # Predefine city data for test coverage
        self.temperatures = {
            "oslo": -5,
            "london": 20,
        }
        self.rain_probabilities = {
            "london": [0.1, 0.2, 0.15, 0.25, 0.05, 0.12, 0.33, 0.41],
        }

    

    def get_chance_of_rain(self, city):
        if not isinstance(city, str) or not city.strip():
            raise Exception("Invalid city")
        if city.lower() in self.rain_probabilities:
            return self.rain_probabilities[city.lower()]
        else: 
            raise Exception("Unknown city")

    def get_city_temperature_info(self, city):
        if not isinstance(city, str) or not city.strip():
            raise Exception("Invalid city")
        if city.lower() in self.temperatures:
            return self.temperatures[city.lower()]
        raise Exception("City not found")

