# Basic If, Elif, Else Examples
# Author: Sai Sukruth Reddy

# 1. Check whether a number is positive, negative or zero
num = 10
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Check voting eligibility
age = 17
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 3. Largest of two numbers
a = 15
b = 20
if a > b:
    print("A is larger")
elif b > a:
    print("B is larger")
else:
    print("Both are equal")

# 4. Check if a number is even or odd
n = 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")
