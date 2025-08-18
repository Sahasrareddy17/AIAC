def sort_numbers():
    # Take input from the user as a space-separated string of numbers
    input_str = input("Enter numbers separated by spaces: ")
    # Convert the input string to a list of integers
    numbers = list(map(int, input_str.strip().split()))
    # Sort the list in ascending order
    numbers.sort()
    # Print the sorted list
    print("Sorted numbers:", numbers)

# Call the function
sort_numbers()


