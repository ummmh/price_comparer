"""Component 1 of Price Comparer
Get budget from user - checking if input is not blank or a string
Created by Janna Lei Eugenio
28/07/2021 - Version 2
"""


def get_budget():
    while True:
        try:
            amount = float(input("How much money do you have?: $"))
            if amount:
                return amount
            break
        # Checks if input is blank or contains string
        except ValueError:
            print("Please input a valid amount (must not contain letters or be"
                  " blank)\n")
            continue


# Main Routine
budget = get_budget()
print("Budget: ${:.2f}".format(budget))
