# Create two separate lists with the same contents
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

print("Separate objects:")
print("x == y:", x == y)
print("x is y:", x is y)
print("id(x):", id(x))
print("id(y):", id(y))

# Make y an alias of x
y = x

print("\nAfter y = x:")
print("x == y:", x == y)
print("x is y:", x is y)
print("id(x):", id(x))
print("id(y):", id(y)) 




