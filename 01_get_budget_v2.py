"""Component 1 of Price Comparer
Get budget from user - checking if input is not blank or a string
Created by Janna Lei Eugenio
28/07/2021 - Version 2 - create function
"""


# Get budget function
def get_budget():
    while True:
        try:
            amount = float(input("How much money do you have?: $"))
            if amount:    # If valid - return amount
                return amount
            break
        # If input contains string or is blank - print error message
        except ValueError:
            print("Please input a valid amount (must not contain letters or be"
                  " blank)\n")
            continue


# Main Routine
budget = get_budget()
print("Budget: ${:.2f}".format(budget))
