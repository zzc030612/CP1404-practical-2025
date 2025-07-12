"""
Guitar class for representing a guitar object.
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of the guitar based on the current year."""
        from datetime import datetime
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50