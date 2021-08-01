"""Component 1 of Price Comparer
Get budget from user - checking if input is not blank or a string
Created by Janna Lei Eugenio
28/07/2021
"""

try:
    # Get budget from user
    budget = float(input("How much money do you have?: $"))
    print("Budget: ${:.2f}".format(budget))
    # Checks if input is blank or contains string
except ValueError:
    print("Invalid entry")
