def greet_user(name, gender):
    """
    Returns a greeting with an appropriate title based on gender.
    - 'Mr.' for males
    - 'Ms.' for females
    - 'Mx.' for any other or unspecified gender
    Gender input is handled case-insensitively.
    """
    # Normalize gender input to lowercase for case-insensitive comparison
    gender = gender.strip().lower()
    if gender == 'male':
        title = 'Mr.'
    elif gender == 'female':
        title = 'Ms.'
    else:
        title = 'Mx.'
    # Return the greeting string
    return f"Hello, {title} {name}!"

# Example calls and their outputs:
print(greet_user("John Doe", "male"))      # Output: Hello, Mr. John Doe!
print(greet_user("Jane Smith", "Female"))  # Output: Hello, Ms. Jane Smith!
print(greet_user("Alex Kim", "nonbinary")) # Output: Hello, Mx. Alex Kim!
print(greet_user("Sam Lee", ""))           # Output: Hello, Mx. Sam Lee!