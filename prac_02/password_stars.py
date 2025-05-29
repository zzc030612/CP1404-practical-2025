MIN_LENGTH = 12
password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print("Password too short")
    password = input("Enter password: ")
print('*' * len(password))