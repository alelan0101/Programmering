#4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
foodTuple = ('pizza', 'pasta', 'salad', 'soup', 'steak')

# Use a for loop to print each food the restaurant offers.
for food in foodTuple:
    print(food)

# Try to modify one of the items, and make sure that Python rejects the change.
# foodTuple[0] = 'spaghetti'
print(foodTuple)


# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foodTuple = ('spaghetti', 'pasta', 'salad', 'soup', 'steak')
for food in foodTuple:
    print(food)
