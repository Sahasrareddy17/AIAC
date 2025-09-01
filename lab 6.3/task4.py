def sum_to_n(n):
    """Calculate the sum of the first n natural numbers."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage:
print(sum_to_n(10))  # Output: 55
