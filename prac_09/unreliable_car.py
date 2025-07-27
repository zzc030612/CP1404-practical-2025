"""
CP1404/CP5632 Practical
UnreliableCar class
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """
        Initialise an UnreliableCar instance, based on parent class Car.
        :param name: string, car name
        :param fuel: int, initial fuel
        :param reliability: float, percentage chance (0-100) the car will drive
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive the car if it is reliable enough.
        :param distance: int, distance to attempt to drive
        :return: int, actual distance driven
        """
        random_number = random.uniform(0, 100)  # Generate a random number between 0 and 100
        if random_number < self.reliability:
            # If the random number is less than reliability, drive as usual
            return super().drive(distance)
        else:
            # Otherwise, the car does not drive
            return 0