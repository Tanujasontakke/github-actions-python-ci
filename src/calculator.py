#Return the sum of a and b.
def add(a, b):
    return a + b

#Return the difference of a and b.
def subtract(a, b):
    return a - b

#Return the division of a by b. Raise an error if b is zero.
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
