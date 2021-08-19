"""Component 4 of Price Comparer
Compare each item - find cheapest, most expensive and recommendation
Created by Janna Lei Eugenio
12/08/2021 - version 3 - allows multiple products to be cheapest, expensive
and recommended
"""


# find recommended function (converted from last version)
def find_recommended(list1):
    recommendation_list = sorted(list1, key=lambda row: row[3])
    recommended = []
    for product in recommendation_list:
        if product[2] <= budget:  # recommends item lower or equal to budget
            recommended.append(product)
        else:                     # keeps checking until recommended found
            continue
    if len(recommended) > 1:
        recommended = find_multiple(recommended, 3, "rec")
        return recommended
    else:
        return recommended


# find multiple recommendation
def find_multiple(list1, check, find):
    list2 = []

    if find == "cheap": # sorts the list by cheapest price
        list1.sort(key=lambda row: row[2])
        amount = list1[0][2]  # amount = lowest price
    elif find == "exp":  # sorts the list by highest price
        list1.sort(key=lambda row: row[2], reverse=True)
        amount = list1[0][2]  # amount = highest price
    else:
        list1.sort(key=lambda row: row[3])  # sorts list by unit price
        amount = list1[0][3]

    for item in list1:
        if item[check] == amount:
            list2.append(item)
        else:
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
budget = float(input("$"))

# Component 4 - compare each product
cheapest = find_multiple(product_list, 2, "cheap")
expensive = find_multiple(product_list, 2, "exp")
recommendation = find_multiple(product_list, 3, "rec")

# Output
print("CHEAPEST: ", cheapest)
print("MOST EXPENSIVE: ", expensive)
print("BEST VALUE: ", recommendation)
if recommendation[0][2] > budget:
    print("\nWARNING! Item with best value is higher than your budget!")
    recommendation = find_recommended(product_list)
    if recommendation is None:
        print("There is no items that fit your budget!")
    else:
        print("RECOMMENDED: ", recommendation)
