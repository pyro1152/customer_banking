# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
        """This function prompts the user to enter the savings and cd account balance, interest rate,
        and the length of months to determine the interest gained.
        It displays the interest earned on the savings and CD accounts and updates the balances.
        """
        # Prompt the user to set the savings balance, interest rate, and months for the savings account.
        savings_balance= int(input("What is your savings balance?"))
        interest_rate= float(input("What is your interest rate?"))
        months= int(input(("Over how many months?")))

                # Call the create_savings_account function and pass the variables from the user.
        savings_account = create_savings_account(savings_balance, interest_rate, months)
        interest_earned = savings_balance * (interest_rate/100 * months/12)
                # Print out the interest earned and updated savings account balance with interest earned for the given months.
        print("interest earned: ", interest_earned )
        print("updated balance: ", savings_balance + interest_earned )
                # Prompt the user to set the CD balance, interest rate, and months for the CD account.
        CD_balance= int(input("What is your CD balance?"))
        CD_interest_rate= float(input("What is your interest rate?"))
        CD_months= int(input(("Over how many months?")))

                # Call the create_cd_account function and pass the variables from the user.
        CD_account, interest_earned = create_cd_account(CD_balance, CD_interest_rate, CD_months)

                # Print out the interest earned and updated CD account balance with interest earned for the given months.
                # print(interest_earned)

        print("interest earned:", interest_earned )

        print("Updated CD Balance", CD_balance+interest_earned )

if __name__ == "__main__":

        # Call the main function  
    main()
