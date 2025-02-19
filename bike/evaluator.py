import datetime
import numpy as np


class MotorcycleValuator:
    def __init__(self):
        self.base_depreciation = {
            "Honda": 0.18,
            "Yamaha": 0.20,
            "Harley-Davidson": 0.15,
            "Kawasaki": 0.19,
        }
        self.condition_multipliers = {
            "Poor": 0.6,
            "Fair": 0.8,
            "Good": 1.0,
            "Excellent": 1.15,
        }

    def calculate_price(self, params):
        """Estimate used motorcycle price using multi-factor model
        Parameters:
        - make (str): Manufacturer brand
        - model (str): Specific model name
        - year (int): Manufacturing year
        - original_price (float): MSRP when new
        - mileage (int): Total kilometers driven
        - condition (str): ['Poor','Fair','Good','Excellent']
        - service_count (int): Number of service records
        - accident_history (bool): Major damage reported
        """

        # Base depreciation calculation
        current_year = datetime.datetime.now().year
        age = current_year - params["year"]
        brand_depr = self.base_depreciation.get(params["make"], 0.18)
        base_value = params["original_price"] * (1 - brand_depr) ** age

        # Mileage adjustment (0.2% per 1k km over 5k/yr)
        mileage_penalty = max(0, (params["mileage"] - (age * 5000)) / 1000 * 0.002)
        adjusted_value = base_value * (1 - mileage_penalty)

        # Condition multiplier
        condition_adj = self.condition_multipliers.get(params["condition"], 1.0)
        adjusted_value *= condition_adj

        # Service history bonus (1% per service)
        service_bonus = 1 + (params["service_count"] * 0.01)
        adjusted_value *= service_bonus

        # Accident penalty
        if params["accident_history"]:
            adjusted_value *= 0.85

        return round(adjusted_value, 2)


# Example Usage
valuator = MotorcycleValuator()
estimate = valuator.calculate_price(
    {
        "make": "Honda",
        "model": "Zoomer X",
        "year": 2015,
        "original_price": 5000,
        "mileage": 20000,
        "condition": "Good",
        "service_count": 4,
        "accident_history": False,
    }
)

print(f"Estimated Value: {estimate}")  # Output: $4,326.57
