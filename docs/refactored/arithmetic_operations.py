import math

def calculate_add(a: int, b: int) -> int:
    return a + b

def calculate_subtract(a: int, b: int) -> int:
    return a - b

def calculate_multiply(a: int, b: int) -> int:
    return a * b

def calculate_divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"Addition: {calculate_add(x, y)}")
    print(f"Subtraction: {calculate_subtract(x, y)}")
    print(f"Multiplication: {calculate_multiply(x, y)}")
    try:
        print(f"Division: {calculate_divide(x, y)}")
    except ValueError as e:
        print(e)