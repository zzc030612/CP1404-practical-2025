"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and flagfall."""
    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, name, fuel, fanciness):
        """
        Initialise a SilverServiceTaxi instance, based on parent class Taxi.
        :param name: string, name of the taxi
        :param fuel: int, initial fuel
        :param fanciness: float, multiplier for price_per_km
        """
        # Calculate the effective price_per_km based on fanciness
        price_per_km = Taxi.price_per_km * fanciness
        super().__init__(name, fuel, price_per_km)  # Pass price_per_km to the parent class
        self.fanciness = fanciness

    def __str__(self):
        """
        Return a string representation of the SilverServiceTaxi.
        Includes flagfall charge.
        """
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """
        Calculate the total fare including flagfall.
        :return: float, total fare for the trip
        """
        return super().get_fare() + self.flagfall