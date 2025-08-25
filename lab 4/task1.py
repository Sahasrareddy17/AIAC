import re

def is_valid_mobile(number):
    """
    Checks if the given mobile number is valid:
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

# Example usage:
if __name__ == "__main__":
    test_numbers = ["9876543210", "1234567890", "8123456789", "5678901234"]
    for num in test_numbers:
        print(f"{num}: {is_valid_mobile(num)}")

