import random

# Line 1: random.randint(5, 20)
# This generates a random integer between 5 and 20, inclusive.
print(random.randint(5, 20))  # Example output: 7

# What did you see on line 1?
# Answer: A random integer between 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 5, and the largest is 20.

# Line 2: random.randrange(3, 10, 2)
# This generates a random number from the range starting at 3, ending before 10, with a step of 2.
print(random.randrange(3, 10, 2))  # Example output: 7

# What did you see on line 2?
# Answer: A random number from the sequence [3, 5, 7, 9].
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 3, and the largest is 9.
# Could line 2 have produced a 4?
# Answer: No, because the step is 2, so only odd numbers in the range are possible.

# Line 3: random.uniform(2.5, 5.5)
# This generates a random floating-point number between 2.5 and 5.5.
print(random.uniform(2.5, 5.5))  # Example output: 3.872639

# What did you see on line 3?
# Answer: A random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Answer: The smallest number is 2.5, and the largest is 5.5.

# Code to produce a random number between 1 and 100 inclusive
random_number = random.randint(1, 100)
print(random_number)  # Example output: 42
