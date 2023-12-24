"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    CD_account = Account(balance, interest)
    #  Hint: You need to add the interest as a value, i.e, 0.

    # Calculate interest earned
    CD_interest_earned = CD_account.balance * interest

    # Update the CD account balance by adding the interest earned
    CD_account.balance += CD_interest_earned
   
    #Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    CD_account.set_balance(CD_account.balance + CD_interest_earned)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    CD_account.set_interest(CD_interest_earned)

    # Return the updated balance and interest earned.
    return CD_account, CD_interest_earned
