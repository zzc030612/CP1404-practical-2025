"""
CP1404/CP5632 Practical
Test UnreliableCar class
"""
from unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""
    # Create a few UnreliableCar objects with different reliability levels
    reliable_car = UnreliableCar("Mostly Reliable", 100, 90)
    unreliable_car = UnreliableCar("Dodgy", 100, 30)

    # Test the reliable car
    print(f"Testing {reliable_car.name}")
    for i in range(10):
        distance_driven = reliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")
    print(f"Final fuel: {reliable_car.fuel} units\n")

    # Test the unreliable car
    print(f"Testing {unreliable_car.name}")
    for i in range(10):
        distance_driven = unreliable_car.drive(10)
        print(f"Attempt {i + 1}: Drove {distance_driven} km")
    print(f"Final fuel: {unreliable_car.fuel} units")


if __name__ == "__main__":
    main()