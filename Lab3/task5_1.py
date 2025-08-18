def temperature_converter():
    """
    Converts a temperature value from one unit to another (Celsius, Fahrenheit, Kelvin, Reaumur).
    Also prints the result in the Reaumur scale.
    
    Instructions:
    1. Enter the temperature value.
    2. Enter the unit to convert from: 'C' for Celsius, 'F' for Fahrenheit, 'K' for Kelvin, 'R' for Reaumur.
    3. Enter the unit to convert to: 'C', 'F', 'K', or 'R'.
    """
    print("Temperature Converter (Celsius, Fahrenheit, Kelvin, Reaumur)")
    value = float(input("Enter the temperature value: "))
    from_unit = input("Enter the unit to convert from (C/F/K/R): ").strip().upper()
    to_unit = input("Enter the unit to convert to (C/F/K/R): ").strip().upper()

    # Convert input to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    elif from_unit == 'R':
        celsius = value * 5/4
    else:
        print("Invalid from_unit. Use 'C', 'F', 'K', or 'R'.")
        return

    # Convert from Celsius to target unit
    if to_unit == 'C':
        result = celsius
    elif to_unit == 'F':
        result = celsius * 9/5 + 32
    elif to_unit == 'K':
        result = celsius + 273.15
    elif to_unit == 'R':
        result = celsius * 4/5
    else:
        print("Invalid to_unit. Use 'C', 'F', 'K', or 'R'.")
        return

    # Always print the value in Reaumur as well
    reaumur = celsius * 4/5

    print(f"{value} {from_unit} is {result:.2f} {to_unit}")
    print(f"In Reaumur scale: {reaumur:.2f} R")

# Example usage:
if __name__ == "__main__":
    temperature_converter()
