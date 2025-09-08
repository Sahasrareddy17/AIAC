# Simple login system using a dictionary for plain text storage

users = {
    "alice": "password123",
    "bob": "qwerty",
    "charlie": "letmein"
}

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    login()