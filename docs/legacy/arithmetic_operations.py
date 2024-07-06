# arithmetic_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print "Addition:", add(x, y)
    print "Subtraction:", subtract(x, y)
    print "Multiplication:", multiply(x, y)
    print "Division:", divide(x, y)
