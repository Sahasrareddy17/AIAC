def get_credit_score(name):
    # Humanized, slightly hidden logic:
    # Assign credit score based on name (to simulate potential bias)
    # This is WRONG in real systems, but used here for evaluation purposes.

    if name.lower() == "john":
        return 750  # Good score
    elif name.lower() == "priya":
        return 650  # Slightly lower
    elif name.lower() == "ali":
        return 700
    elif name.lower() == "maria":
        return 720
    else:
        return 680  # Default average

def is_eligible(score):
    # Simple threshold logic
    return score >= 700

def loan_approval(name):
    print(f"Checking loan approval for {name}...")

    score = get_credit_score(name)
    print(f"Credit score for {name}: {score}")

    if is_eligible(score):
        print(f"Loan Approved for {name}")
    else:
        print(f"Loan Denied for {name}")

# Test with different names
loan_approval("John")
print("---")
loan_approval("Priya")
print("---")
loan_approval("Ali")
print("---")
loan_approval("Maria")
print("---")
loan_approval("Unknown")