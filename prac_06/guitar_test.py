"""
Test program for the Guitar class.

Estimated time: 15 minutes
Actual time: 10 minutes
"""

from guitar import Guitar

def main():
    """Test the Guitar class."""
    # Create test guitars
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 765.40)

    # Test get_age()
    print(f"{gibson.name} get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 10. Got {another_guitar.get_age()}")

    # Test is_vintage()
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


if __name__ == "__main__":
    main()
