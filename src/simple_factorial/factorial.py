# factorial.py

def factorial(n):
    """Calculate the factorial of a non-negative integer."""
    n = int(n)
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    while True:
        num = input("Enter a non-negative integer (or 'q' to quit): ")
        if num.lower() == 'q':
            break
        result = calculate_factorial(num)
        print(result)