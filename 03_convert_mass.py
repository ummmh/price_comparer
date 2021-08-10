"""Component 3 of Price Comparer
Calculate the comparisons
Created by Janna Lei Eugenio
4/08/2021
"""

# List from sample data
product_list = [['Sea Salt Crackers', (185.0, 'g'), 2.0],
                ['Griffin Snax', (250.0, 'g'), 2.5],
                ['Pizza Shapes', (190.0, 'g'), 3.3],
                ['Arnotts Cheds', (250.0, 'g'), 3.99],
                ['Rosemary Wheat', (170.0, 'g'), 2.0],
                ['Original Rice Crackers', (100.0, 'g'), 1.65]]


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
     # print for testing
    print("{}: {}kg ${:.2f}/kg".format(product[0], unit_weight, unit_price))
