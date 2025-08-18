def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Find the factorial of the number 8 using recursion
result = factorial_recursive(8)
print(f"The factorial of 8 is {result}")



