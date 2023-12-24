"""Imports the SavingsAccount class and attributes from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE


    account = Account(balance, interest_rate)
    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * interest_rate
    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    savings_account_balance= balance + interest_earned
    # Create an instance of the SavingsAccount class
savings_account = Account(1000, 0.05)

# Calculate the interest earned
interest_earned = savings_account.balance * savings_account.interest

# Update the savings account balance by adding the interest earned
updated_balance = savings_account.balance + interest_earned

# Pass the updated balance to the set_balance method
savings_account.set_balance(updated_balance)

# Print the updated savings account balance
print(savings_account.balance)
# Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
savings_account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
class SavingsAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def set_interest(self, interest_earned):
        self.interest_rate = interest_earned

# Create an instance of the SavingsAccount class
savings_account = SavingsAccount(1000, 0.05)

# Pass the interest_earned to the set_interest method
interest_earned = 0.08
savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
def calculate_future_value(current_loan_value, months_remaining, annual_interest_rate):
    # Calculate the interest earned
    interest_earned = current_loan_value * (annual_interest_rate / 12) * months_remaining
    
    # Calculate the updated balance
    updated_balance = current_loan_value + interest_earned
    
    # Return the updated balance and interest earned
    return updated_balance, interest_earned
new_car_loan = {
    "current_loan_value" : 24000,
    "months_remaining" : 6,
    "annual_interest_rate" : 0.085,
}

updated_balance, interest_earned = calculate_future_value(new_car_loan["current_loan_value"], new_car_loan["months_remaining"], new_car_loan["annual_interest_rate"])

print("Updated Balance:", updated_balance)
print("Interest Earned:", interest_earned)