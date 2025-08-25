def factorial(n):
    if n < 0:
        raise ValueError("Error: Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
# print(factorial(5))  # Output: 120
# print(factorial(0))  # Output: 1
# print(factorial(-3)) # Raises ValueError