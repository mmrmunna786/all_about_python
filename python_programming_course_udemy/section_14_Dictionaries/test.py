# instructor = {
#     "name": "John Doe",
#     "age": 35,
#     "courses": ["Python", "Data Science", "Machine Learning"]
# }

# print("name" in instructor.keys())
# print("John Doe" in instructor.values())

# # This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

# #DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# # YOUR CODE GOES BELOW:

# if food in bakery_stock.keys():
#     print( f"{bakery_stock[food]} {food}s left " )
# else:
#     print( "we dont make that" )
 
inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = inventory.copy()


# add the value 18 to stock_list under the key "cookie"

stock_list.update({"cookie": 18})

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")