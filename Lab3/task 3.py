def calculate_power_bill(units):
    """
    Calculates the power bill for a given number of units.
    Example slab (can be adjusted as needed):
      - First 100 units: Rs. 5 per unit
      - Next 100 units (101-200): Rs. 7 per unit
      - Above 200 units: Rs. 10 per unit
    """
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

# Example usage:
units = int(input("Enter the number of units consumed: "))
total_bill = calculate_power_bill(units)
print(f"Total power bill for {units} units is: Rs. {total_bill}")
