"""Component 1 of Price Comparer
Get budget from user - checking if input is not blank or a string
Created by Janna Lei Eugenio
2/08/2021 - Version 3 - create not blank function
"""


# Not Blank Function
def not_blank(question, string, error):
    letter = False
    while True:
        ask = input(question)
        if not string:  # If "string" is false = it checks for letters
            try:
                return float(ask)
            except ValueError:
                letter = True
        if not ask or letter is True:  # If input is blank (or has digits)
            print(error)  # Prints error message
        else:
            return ask


# Main Routine
budget = not_blank("How much money do you have?: $", False, "Please input a"
                                                            " valid amount "
                                                            "(must not contain"
                                                            " letters or be "
                                                            "blank)\n")
print("Budget: ${:.2f}".format(budget))
