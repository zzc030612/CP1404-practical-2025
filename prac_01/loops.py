# Loop to display all odd numbers between 1 and 20
print("Odd numbers between 1 and 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Question a: Count in 10s from 0 to 100
print("\n(a) Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Question b: Count down from 20 to 1
print("\n(b) Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Question c: Print n stars on one line
print("\n(c) Print n stars on one line:")
n = int(input("Number of stars: "))  # Get user input
for i in range(n):
    print('*', end='')  # Print asterisks without line breaks
print()  # Break a line to separate the output

# Question d: Print n lines of increasing stars
print("\n(d) Print n lines of increasing stars:")
for i in range(1, n + 1):  # From 1 to n (including n)
    print('*' * i)  # Print i asterisks and each line will break automatically