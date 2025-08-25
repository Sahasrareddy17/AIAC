def is_valid_mobile_number(number):
    """
    Checks if the given number is a valid mobile number:
    - Must be a string of 10 digits
    - Must start with 6, 7, 8, or 9
    """
    if isinstance(number, str) and len(number) == 10 and number.isdigit():
        return number[0] in {'6', '7', '8', '9'}
    return False
