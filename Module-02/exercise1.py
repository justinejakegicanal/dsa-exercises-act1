def ex6():
    i = 0
    while i < 5:
        print(i)
        i += 1
        if i == 3:
            break
    else:
        print(0)

ex6()
print(True or False and False)
print((True or False) and False)

value = 12
print(value > 10 or value <= 5 and value != 12)
print((value > 10 or value <= 5) and value != 12)

# Output:
# 0
# 1
# 2
# True
# False
# True
# False