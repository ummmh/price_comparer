"""Component 4 of Price Comparer
Compare each item - find cheapest, most expensive and recommendation
Created by Janna Lei Eugenio
11/08/2021 - version 2 - finds recommendation
"""

# List from sample data (with unit price)
product_list = [['Sea Salt Crackers', (185.0, 'g'), 2.0, 10.81081081081081],
                ['Griffin Snax', (250.0, 'g'), 2.5, 10.0],
                ['Pizza Shapes', (190.0, 'g'), 3.3, 17.36842105263158],
                ['Arnotts Cheds', (250.0, 'g'), 3.99, 15.96],
                ['Rosemary Wheat', (170.0, 'g'), 2.0, 11.76470588235294],
                ['Original Rice Crackers', (100.0, 'g'), 1.65,
                 16.499999999999996]]

# Component 4 - compare each product (find recommended from unit price)
# Input budget for testing (component 1)
budget = float(input("budget: $"))

# Sorts the list by the cheapest unit price
recommendation_list = sorted(product_list, key=lambda row: row[3])
for product in recommendation_list:
    if product[2] <= budget:  # recommends item lower or equal to budget
        recommendation = product
        break
    else:                     # keeps checking until recommended found
        continue

# prints recommendation
print("Recommended: ", recommendation)
