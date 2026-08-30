import math

def area_of_circle(r):
    return math.pi * (r ** 2)

radius = float(input("Enter radius: "))
print("Area:", area_of_circle(radius))