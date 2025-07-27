"""
CP1404/CP5632 Practical
Test SilverServiceTaxi class
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""
    # Create a SilverServiceTaxi with fanciness of 2
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18 km
    fancy_taxi.drive(18)

    # Print details of the taxi
    print(fancy_taxi)  # Expect: Hummer, fuel=182, odo=18, 18km on current fare, $2.46/km plus flagfall of $4.50

    # Calculate and print the fare
    fare = fancy_taxi.get_fare()
    print(f"Fare: ${fare:.2f}")  # Expect: Fare: $48.78

    # Assert tests to verify functionality
    assert fancy_taxi.price_per_km == 2.46, "Price per km calculation is incorrect"
    assert fare == 48.78, "Fare calculation is incorrect"


if __name__ == "__main__":
    main()