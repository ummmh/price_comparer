"""Component 2 of Price Comparer
Get a list of products with their volume and price for comparison
Created by Janna Lei Eugenio
3/08/2021 - Version 2 - checks for valid input and re-asks
"""


# Not Blank Function
def not_blank(question, string, error):
    letter = False
    while True:
        ask = input(question)
        if not string:          # If "string" is false = it checks for letters
            try:
                return float(ask)
            except ValueError:
                letter = True
        if not ask or letter is True:  # If input is blank (or has digits)
            print(error)               # Prints error message
        else:
            return ask


# Main Routine
# Set up list to store products
product_list = []

while True:
    product = not_blank("Product: ", True, "Product cannot be blank").title()
    if product == "X":
        break
    mass = not_blank("Mass (ml/g): ", False, "Please enter a valid number")
    price = not_blank("Price: $", False, "Please enter a valid number")
    print()
    product_list.append([product, mass, price])  # Adds product, mass & price to list

print(product_list)
