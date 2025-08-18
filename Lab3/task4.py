users_db = {}

def register_user(username, password):
    """
    Registers a new user with the given username and password.
    Returns True if registration is successful, False if username already exists.
    """
    if username in users_db:
        print("Username already exists. Please choose a different username.")
        return False
    users_db[username] = password
    print("Registration successful!")
    return True

def login_user(username, password):
    """
    Logs in an existing user by checking username and password.
    Returns True if login is successful, False otherwise.
    """
    if username not in users_db:
        print("Username does not exist.")
        return False
    if users_db[username] != password:
        print("Incorrect password.")
        return False
    print("Login successful!")
    return True

# Example usage:
if __name__ == "__main__":
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            uname = input("Enter new username: ").strip()
            pwd = input("Enter new password: ").strip()
            register_user(uname, pwd)
        elif choice == '2':
            uname = input("Enter username: ").strip()
            pwd = input("Enter password: ").strip()
            login_user(uname, pwd)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
