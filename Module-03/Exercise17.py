# Original scores list
scores = [72, 55, 89, 64, 91, 48, 77, 60]

# Pass threshold: 60
# 1. Create passed using a filtered list comprehension
passed = [score for score in scores if score >= 60]

# 2. Create squares using a regular list comprehension
squares = [score ** 2 for score in scores]

# 3. Print all three lists
print("Original scores:", scores)
print("Passed scores:  ", passed)
print("Squared scores: ", squares)

