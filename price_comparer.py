"""Price Comparer - fully working program combining all 5 components
First version of fully working program - not tested for usability
Created by Janna Lei Eugenio
19/08/2021
"""

import re


# Functions
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


# Get volume function
def get_volume():
    # The expected format for the volume input
    volume_regex = r"(\d+(?:\.\d+)?)(\w+)"

    while True:
        try:
            entry = not_blank("Volume: ", True, "Please enter a valid number")
            mass = re.match(volume_regex, entry)
            if mass:
                amount = float(mass.group(1))  # If input matches the regex
                unit = mass.group(2)           # splits it into amount and unit
                product_mass = (amount, unit)
                if unit == "g" or unit == "kg" or unit == "ml":  # Only accepts
                    return product_mass                           # g, kg or ml
                else:
                    print("Invalid unit (please only enter g, kg, or ml")
                    continue   # Re-asks if invalid unit
            else:
                try:                               # If it doesn't match the
                    product_mass = entry.split()     # regex: tries to split
                    amount = float(product_mass[0])  # into amount and unit
                    unit = product_mass[1]
                    product_mass = (amount, unit)
                    if unit == "g" or unit == "kg" or unit == "ml":
                        return product_mass
                    else:
                        print("Invalid unit (please only enter g, kg, or ml")
                        continue
                except ValueError:  # re-asks if invalid input
                    print("Please enter a valid amount")
        except IndexError:
            print("Please enter a valid amount")


# Find recommended function
def find_recommended(list1):
    recommendation_list = sorted(list1, key=lambda row: row[3])
    for item in recommendation_list:
        if item[2] <= budget:  # recommends item lower or equal to budget
            return item
        else:                     # keeps checking until recommended found
            continue


# Find multiple recommendations
def find_multiple(list1, check, find):
    list2 = []

    if find == "cheap": # sorts the list by cheapest price
        low = sorted(list1, key=lambda row: row[2])
        amount = low[0][2]  # amount = lowest price
    else:  # sorts the list by highest price
        high = sorted(list1, key=lambda row: row[2], reverse=True)
        amount = high[0][2]  # amount = highest price

    # checks how many items in list is equal to set amount
    for item in list1:
        if item[check] == amount:
            list2.append(item)
        else:  # breaks loop if there are none left
            break
    return list2


# Main Routine
# Set up list to store products
product_list = []

# Ask user for budget
budget = not_blank("How much money do you have?: $", False, "Please input a"
                                                            " valid amount "
                                                            "(must not contain"
                                                            " letters or be "
                                                            "blank)\n")
# Get products to compare from user
print()
while True:
    product = not_blank("Product: ", True, "Product cannot be blank").title()
    if product == "X":  # Breaks loop when 'X' is entered
        break
    volume = get_volume()  # Splits the unit and volume amount
    price = not_blank("Price: $", False, "Please enter a valid number")
    print()
    # Adds product, mass & price to list
    product_list.append([product, volume, price])

# Converts the volume to kgs and finds unit price
for product in product_list:
    # find the mass in the list
    mass = product[1][0]
    # converting the weight to kg
    if product[1][1] == 'g' or product[1][1] == 'ml': # if mass in g or ml
        # noinspection PyTypeChecker
        unit_weight = mass / 1000
    else:                                  # if its already in kg leave as is
        unit_weight = mass

    # calculates how much the product costs per kg
    unit_price = product[2] / unit_weight
    product.append(unit_price)      # stores unit price with the product

# Compare each product and finds recommendation
cheapest = find_multiple(product_list, 2, "cheap")
expensive = find_multiple(product_list, 2, "x")
# sorts list by unit price and price - first item is recommended
recommendation = sorted(product_list, key=lambda row: (row[3], row [2]))[0]

# End summary
print("---------------------------END SUMMARY--------------------------------")
# Budget
print("\nBUDGET: ${:.2f}".format(budget))

# Product List
print("\nPRODUCT LIST:")
for product in product_list:
    print("{}. {} - PRICE: ${:.2f} - AVERAGE PRICE: ${:.2f}"
          .format(product_list.index(product) + 1, product[0],
                  product[2], product[3]))

# Print recommended
print("\nCHEAPEST:")
for product in cheapest:
    print("{} - ${:.2f}".format(product[0], product[2]))

print("\nMOST EXPENSIVE:")
for product in expensive:
    print("{} - ${:.2f}".format(product[0], product[2]))

print("\nBEST VALUE:\n{} - ${:.2f} (price per kg: ${:.2f})"
      .format(recommendation[0], recommendation[2], recommendation[3]))


# in case the best value is higher than budget
if recommendation[2] > budget:
    print("\n!!! WARNING! Item with best value is higher than your budget !!!")
    recommendation = find_recommended(product_list)
    if recommendation is None:  # if there's no recommended
        print("There is no items that fit your budget!")
    else:
        print("RECOMMENDED: {} - ${:.2f} (price per kg: ${:.2f})"
              .format(recommendation[0], recommendation[2], recommendation[3]))
