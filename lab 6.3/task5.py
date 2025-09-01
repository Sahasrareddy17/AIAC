class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount instance.
        :param initial_balance: Starting balance for the account (default is 0)
        """
        self.balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        :param amount: Amount to deposit (must be positive)
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        :param amount: Amount to withdraw (must be positive and <= current balance)
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """
        Return the current account balance.
        """
        return self.balance

# Example usage:
if __name__ == "__main__":
    # Create a new bank account with an initial balance of 100
    account = BankAccount(100)
    account.deposit(50)         # Deposit 50
    account.withdraw(30)        # Withdraw 30
    print("Balance:", account.get_balance())  # Print current balance

"""
Analysis:
- The BankAccount class encapsulates the concept of a bank account.
- The constructor (__init__) initializes the account with an optional starting balance.
- deposit() adds a positive amount to the balance.
- withdraw() subtracts a positive amount from the balance if sufficient funds exist.
- get_balance() returns the current balance.
- Input validation ensures only positive amounts are processed.
- Example usage demonstrates creating an account, depositing, withdrawing, and checking balance.
"""