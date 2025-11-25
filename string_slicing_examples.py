# String Indexing & Slicing Examples
# Author: Sai Sukruth Reddy

# Basic string
text = "pythonprogramming"

# Indexing
print("First letter:", text[0])
print("Last letter:", text[-1])
print("5th letter:", text[4])
print("Second last letter:", text[-2])

# Basic slicing
print("First 6 letters:", text[0:6])
print("Last 7 letters:", text[-7:])
print("Middle part:", text[6:12])

# Slicing with step
print("Every 2nd letter:", text[0:len(text):2])
print("Reverse string:", text[::-1])
print("Reverse every 2nd letter:", text[::-2])

# Practical example: Extract word
sentence = "Learn Python Programming"
print("Extracted word:", sentence[6:12])   # Python

# Practical example: Masking last 4 characters
phone = "9876543210"
masked = phone[:-4] + "****"
print("Masked phone number:", masked)
