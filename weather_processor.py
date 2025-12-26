class WeatherProcessor:
            def __init__(self, fetcher):
                self.fetcher = fetcher
                # Time slots: 0AM, 3AM, 6AM, 9AM, 12PM, 3PM, 6PM, 9PM
                self.time_slots = [0, 3, 6, 9, 12, 15, 18, 21]
            
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
            
            def get_rain_forecast(self, city, hour):
                """
                Gets rain forecast for a city at a specific hour.
                Finds the closest time slot and returns a forecast based on the probability.
                """
                # Get rain probabilities from the fetcher
                probabilities = self.fetcher.get_chance_of_rain(city)
                
                if probabilities is None or len(probabilities) != len(self.time_slots):
                    return f"Rain data for {city} not available."
                
                # Find the closest time slot to the given hour
                # This line finds the index of the time slot in self.time_slots that is closest to the given hour.
                # It does this by iterating over all indices of self.time_slots and selecting the index where
                # the absolute difference between the time slot and the hour is minimized.
                closest_index = min(
                    range(len(self.time_slots)), 
                    key=lambda i: abs(self.time_slots[i] - hour)
                )
                closest_time = self.time_slots[closest_index]
                probability = probabilities[closest_index]
                
                # Generate forecast based on probability
                if probability >= 0.8:
                    forecast = "high"
                    message = f"There's a high chance of rain in {city} around {closest_time}:00 ({probability*100:.0f}% probability)."
                elif probability >= 0.5:
                    forecast = "moderate"
                    message = f"There's a moderate chance of rain in {city} around {closest_time}:00 ({probability*100:.0f}% probability)."
                elif probability >= 0.2:
                    forecast = "low"
                    message = f"There's a low chance of rain in {city} around {closest_time}:00 ({probability*100:.0f}% probability)."
                else:
                    forecast = "very low"
                    message = f"There's a very low chance of rain in {city} around {closest_time}:00 ({probability*100:.0f}% probability)."
                
                return message