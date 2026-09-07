x = [1, 2, 3]
y = x.copy()
y.append(4)

# Display lists, identities, and identity comparison
print("x:", x)
print("id(x):", id(x))
print("y:", y)
print("id(y):", id(y))
print("x is y:", x is y)

