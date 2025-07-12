"""
Guitar class for storing details about guitars.

Estimated time: 20 minutes
Actual time: 15 minutes
"""

class Guitar:
    """Represent a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar in years."""
        current_year = 2023  # Update this to the current year if needed
        return current_year - self.year