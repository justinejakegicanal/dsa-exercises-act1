number = 5
while number > 1:
    if number % 2 == 1:
        number = number * 3 + 1
    else:
        number = number // 2
    print(number, ",", end=" ")
else:
    print("EX3-END")

# Output:
# 16 , 8 , 4 , 2 , 1 , EX3-END