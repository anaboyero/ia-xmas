class WeatherProcessor:
    # Constants for rain forecast probability thresholds
    HIGH_RAIN_PROBABILITY = 0.8
    MODERATE_RAIN_PROBABILITY = 0.5
    LOW_RAIN_PROBABILITY = 0.2

    def _validate_temperature(self, temp):
        """Validates that temperature is a number and not None."""
        if temp is None:
            raise ValueError("Temperature cannot be None")
        if not isinstance(temp, (int, float)):
            raise TypeError("Temperature must be a number")

    def __init__(self, fetcher):
        self.fetcher = fetcher
        # Time slots: 0AM, 3AM, 6AM, 9AM, 12PM, 3PM, 6PM, 9PM
        self.time_slots = [0, 3, 6, 9, 12, 15, 18, 21]

    # ========== VALIDATION METHODS ==========
    # All validation is separated into dedicated methods for consistency and reusability
    
    def _validate_city(self, city):
        """Validates that city is a non-empty string."""
        if city is None:
            raise ValueError("City cannot be None")
        if not isinstance(city, str):
            raise TypeError("City must be a string")
        if not city.strip():
            raise ValueError("City cannot be empty")

    def _validate_hour(self, hour):
        """Validates that hour is an integer in valid range (0-23)."""
        if not isinstance(hour, int):
            raise TypeError("Hour must be int")
        if hour < 0 or hour > 23:
            raise ValueError(f"Hour must be between 0 and 23, got {hour}")

    def _validate_rain_probabilities(self, probabilities):
        """Validates that probabilities list is valid."""
        if probabilities is None:
            raise ValueError("Rain probabilities not available")
        if not isinstance(probabilities, list):
            raise TypeError("Probabilities must be a list")
        if len(probabilities) != len(self.time_slots):
            raise ValueError(f"Probabilities length invalid, expected {len(self.time_slots)}")
        for i, p in enumerate(probabilities):
            if not (isinstance(p, float) or isinstance(p, int)):
                raise TypeError(f"Probability at index {i} is not a number")
            if p < 0 or p > 1:
                raise ValueError(f"Probability at index {i} out of bounds (must be between 0 and 1)")

    def _validate_temperature(self, temp):
        """Validates that temperature is a number (if not None)."""
        if temp is not None and not isinstance(temp, (int, float)):
            raise TypeError("Temperature must be a number or None")

    # ========== BUSINESS LOGIC METHODS ==========
    # Business logic is cleanly separated from validation
    
    def _find_closest_time_slot(self, hour):
        """Finds the closest time slot to the given hour."""
        closest_index = min(
            range(len(self.time_slots)), 
            key=lambda i: abs(self.time_slots[i] - hour)
        )
        return closest_index, self.time_slots[closest_index]

    def _categorize_rain_probability(self, probability):
        """Categorizes a probability value into a forecast level."""
        if probability >= self.HIGH_RAIN_PROBABILITY:
            return "high"
        elif probability >= self.MODERATE_RAIN_PROBABILITY:
            return "moderate"
        elif probability >= self.LOW_RAIN_PROBABILITY:
            return "low"
        else:
            return "very low"

    def _format_temperature_message(self, city, temp):
        """Formats temperature information into a message."""
        if temp < 0:
            return f"It's freezing in {city}: {temp}°C"
        elif temp > 30:
            return f"It's hot in {city}: {temp}°C"
        else:
            return f"The temperature in {city} is {temp}°C"

    # ========== PUBLIC API METHODS ==========
    # Public methods validate inputs first, then delegate to business logic
    
    def get_rain_forecast(self, city, hour):
        """
        Gets rain forecast for a city at a specific hour.
        Finds the closest time slot and returns a forecast based on the probability.
        Raises Exception on invalid input as per test_weather_processor.py.
        """
        # Validate all inputs upfront (fail fast)
        self._validate_city(city)
        self._validate_hour(hour)
        
        # Fetch data
        probabilities = self.fetcher.get_chance_of_rain(city)
        self._validate_rain_probabilities(probabilities)

        # Business logic (validation complete)
        closest_index, closest_time = self._find_closest_time_slot(hour)
        probability = probabilities[closest_index]
        forecast = self._categorize_rain_probability(probability)

        return f"There's a {forecast} chance of rain in {city} around {closest_time}:00 ({probability*100:.0f}% probability)."
    
    def get_city_temperature_info(self, city):
        """
        Gets temperature information for a city.
        Returns a formatted message describing the temperature.
        """
        # Validate input upfront
        self._validate_city(city)
        
        # Fetch data
        temp = self.fetcher.get_current_temperature(city)
        self._validate_temperature(temp)
        
        # Business logic (validation complete)
        if temp is None:
            return f"Temperature data for {city} not available."
        
        return self._format_temperature_message(city, temp)