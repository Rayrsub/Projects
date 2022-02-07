#ask the user to input information.
flowerpot = int(input('how many flowerpots?'))
flower_seeds = int(input('how many packs of flower seeds?'))
soil = int(input('how many bags of soil?'))

#cost per item.
flowerpot_price = 4.00
flower_seeds_price = 1.00
soil_price = 5.00

#sales tax
tax_rate = 0.06

#calculation of items cost
cost_of_items =(flowerpot * flowerpot_price) + (flower_seeds * flower_seeds_price) + (soil * soil_price)
print (cost_of_items)

#total cost with tax
total_cost = (cost_of_items * tax_rate) + cost_of_items

print(total_cost)
