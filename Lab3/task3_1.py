def calculate_power_bill(units, customer_type):
    """
    Calculates the power bill for a given number of units and customer type.
    Slabs:
      - First 100 units
      - Next 100 units (101-200)
      - Above 200 units

    Rates (example):
      - 'residential': 5, 7, 10
      - 'commercial': 8, 10, 15
      - 'industrial': 10, 13, 18
    """
    rates = {
        'residential': [5, 7, 10],
        'commercial': [8, 10, 15],
        'industrial': [10, 13, 18]
    }
    if customer_type not in rates:
        raise ValueError("Invalid customer type. Choose from 'residential', 'commercial', or 'industrial'.")

    r1, r2, r3 = rates[customer_type]
    bill = 0
    if units <= 100:
        bill = units * r1
    elif units <= 200:
        bill = (100 * r1) + ((units - 100) * r2)
    else:
        bill = (100 * r1) + (100 * r2) + ((units - 200) * r3)
    return bill

# Example usage:
units = int(input("Enter the number of units consumed: "))
customer_type = input("Enter customer type (residential/commercial/industrial): ").strip().lower()
try:
    total_bill = calculate_power_bill(units, customer_type)
    print(f"Total power bill for {units} units ({customer_type}) is: Rs. {total_bill}")
except ValueError as e:
    print(e)
