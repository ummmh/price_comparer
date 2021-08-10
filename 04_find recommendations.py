"""Component 4 of Price Comparer
Compare each item - find cheapest, most expensive and recommendation
Created by Janna Lei Eugenio
9/08/2021
"""

# List from sample data
product_list = [['Sea Salt Crackers', (185.0, 'g'), 2.0],
                ['Griffin Snax', (250.0, 'g'), 2.5],
                ['Pizza Shapes', (190.0, 'g'), 3.3],
                ['Arnotts Cheds', (250.0, 'g'), 3.99],
                ['Rosemary Wheat', (170.0, 'g'), 2.0],
                ['Original Rice Crackers', (100.0, 'g'), 1.65]]

# Component 4 - compare each product
product_list.sort(key=lambda row: row[2])   # sorts the list by price
cheapest = product_list[0]                  # cheapest is at start of list
expensive = product_list[-1]                # most expensive is last
# print for testing
print("Cheapest: {}\nMost Expensive: {}".format(cheapest, expensive))
