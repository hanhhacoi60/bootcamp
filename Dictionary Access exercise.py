# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

# My original solution with f strings
if food in bakery_stock:
    print(f"{food}: There are {bakery_stock[food]} left")
else:
    print(f"We don't make {food}")

# My solution with .format
if food in bakery_stock:
    print("{}: There are {} left".format(food, bakery_stock[food]))
else:
    print("We don't make {}".format(food))

# Colt's solution with .get() instead of in
quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")
