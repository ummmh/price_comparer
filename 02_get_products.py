"""Component 2 of Price Comparer
Get a list of products with their volume and price for comparison
Created by Janna Lei Eugenio
2/08/2021
"""

# Set up list to store products
product_list = []

while True:
    product = input("Enter product name: ").title()
    if product == "X":  # If the input is x - ends list
        break
    mass = float(input("Enter volume of product (g/ml): "))
    price = float(input("Enter price of product: $"))
    print()
    product_list.append([product, mass, price])  # Adds product, mass & price to list

print(product_list)
