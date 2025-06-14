import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
RANDOM_NUMBER = 6

quick_pick_number = int(input("Enter number of quick picks: "))

while quick_pick_number <= 0:
    print("Quick pick number is > 0")
    quick_pick_number = int(input("Enter number of quick picks: "))

for i in range(quick_pick_number):
    numbers = []
    for j in range(RANDOM_NUMBER):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(number)
    numbers.sort()
    print(" ".join(f"{number:2}" for number in numbers))