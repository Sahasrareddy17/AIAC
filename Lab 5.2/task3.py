# Function to calculate the nth Fibonacci number using recursion

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (must be >= 0).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    # Base cases: fibonacci(0) = 0, fibonacci(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
if __name__ == "__main__":
    num = 6
    print(f"The {num}th Fibonacci number is {fibonacci(num)}")