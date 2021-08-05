"""Component 2 of Price Comparer
Get a list of products with their volume and price for comparison
Created by Janna Lei Eugenio
4/08/2021 - Version 4 - entire component with volume function
"""

import re


# Check Blank Function
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


# Get volume function
def get_volume():
    # The expected format for the volume input
    volume_regex = r"(\d+(?:\.\d+)?)(\w+)"

    while True:
        entry = not_blank("Volume: ", True, "Please enter a valid number")
        mass = re.match(volume_regex, entry)
        if mass:
            amount = float(mass.group(1))          # If input matches the regex
            unit = mass.group(2)                   # splits it into amount and unit
            product_mass = (amount, unit)
            if unit == "g" or unit == "kg" or unit == "ml":   # Only accepts g,
                return product_mass                           # kg or ml
            else:
                print("Invalid unit (please only enter g, kg, or ml")
                continue                              # Re-asks if invalid unit
        else:
            try:                               # If it doesn't match the regex:
                product_mass = entry.split()   # tries to split into amount and unit
                amount = float(product_mass[0])
                unit = product_mass[1]
                product_mass = (amount, unit)
                if unit == "g" or unit == "kg" or unit == "ml":
                    return product_mass
                else:
                    print("Invalid unit (please only enter g, kg, or ml")
                    continue
            except ValueError:                        # re-asks if invalid input
                print("Please enter a valid amount")


# Main Routine
# Set up list to store products
product_list = []

while True:
    product = not_blank("Product: ", True, "Product cannot be blank").title()
    if product == "X":
        break
    volume = get_volume()
    price = not_blank("Price: $", False, "Please enter a valid number")
    print()
    product_list.append([product, volume, price])  # Adds product, mass & price to list

print(product_list)
