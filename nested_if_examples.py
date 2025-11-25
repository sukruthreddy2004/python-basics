# Nested If Statement Examples
# Author: Sai Sukruth Reddy

# 1. Check if a person is eligible for a loan
age = 25
income = 40000

if age >= 18:
    if income >= 30000:
        print("Eligible for loan")
    else:
        print("Age okay, but income too low")
else:
    print("Not eligible due to age")

# 2. Check if a number is positive, then check if it's even or odd
num = 12

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
else:
    print("Not a positive number")

# 3. Login simulation
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username not found")
