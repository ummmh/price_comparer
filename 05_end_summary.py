"""Component 5 of Price Comparer
Prints the results to the user
Created by Janna Lei Eugenio
19/08/2021
"""


# COMPONENT 4 (for testing)
# find recommended function (converted from last version)
def find_recommended(list1):
    recommendation_list = sorted(list1, key=lambda row: row[3])
    for product in recommendation_list:
        if product[2] <= budget:  # recommends item lower or equal to budget
            return product
        else:                     # keeps checking until recommended found
            continue


# find multiple recommendation
def find_multiple(list1, check, find):
    list2 = []

    if find == "cheap": # sorts the list by cheapest price
        list1.sort(key=lambda row: row[2])
        amount = list1[0][2]  # amount = lowest price
    else:  # sorts the list by highest price
        list1.sort(key=lambda row: row[2], reverse=True)
        amount = list1[0][2]  # amount = highest price

    # checks how many items in list is equal to set amount
    for item in list1:
        if item[check] == amount:
            list2.append(item)
        else:  # breaks loop if there are none left
            break
    return list2


# Main Routine
# List from sample data (with unit price)
product_list = [['Sea Salt Crackers', (185.0, 'g'), 2.0, 10.81081081081081],
                ['Griffin Snax', (250.0, 'g'), 2.5, 10.0],
                ['Pizza Shapes', (190.0, 'g'), 3.3, 17.36842105263158],
                ['Arnotts Cheds', (250.0, 'g'), 3.99, 15.96],
                ['Rosemary Wheat', (170.0, 'g'), 2.0, 11.76470588235294],
                ['Original Rice Crackers', (100.0, 'g'), 1.65,
                 16.499999999999996]]


# Input budget for testing (component 1)
budget = 2

# Component 4 - compare each product
cheapest = find_multiple(product_list, 2, "cheap")
expensive = find_multiple(product_list, 2, "exp")
# sorts list by unit price and price - first item is recommended
recommendation = sorted(product_list, key=lambda row: (row[3], row [2]))[0]


# END SUMMARY
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
