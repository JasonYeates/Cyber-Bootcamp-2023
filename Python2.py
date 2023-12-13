# Sample values for demonstration
a = 5
b = 10

# Equals: a == b
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Not Equals: a != b
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")

# Less than: a < b
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Less than or equal to: a <= b
if a <= b:
    print("a is less than or equal to b")
else:
    print("a is greater than b")

# Greater than: a > b
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# Greater than or equal to: a >= b
if a >= b:
    print("a is greater than or equal to b")
else:
    print("a is less than b")

# If statement with a logical conditional and elif
c = 7
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# If statement with both elif and else
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# If statement with and between conditions
if a > 0 and b > 0:
    print("Both a and b are positive")
else:
    print("At least one of a or b is not positive")

# If statement with or between conditions
if a > 0 or b > 0:
    print("At least one of a or b is positive")
else:
    print("Both a and b are not positive")

# Nested if statement
if a > 0:
    if b > 0:
        print("Both a and b are positive")
    else:
        print("a is positive, but b is not")
else:
    print("a is not positive")

# If statement with pass
if a == b:
    pass
else:
    print("a is not equal to b")
