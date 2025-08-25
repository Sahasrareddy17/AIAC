def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    Returns 1 for n == 0.
    Prints an error message and returns None for negative numbers.
    """
    if not isinstance(n, int):
        print("Error: Input must be an integer.")
        return None
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
