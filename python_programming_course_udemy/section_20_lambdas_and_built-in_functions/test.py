# def decrement_list( list_of_nums ):
#     # It should return a copy of the list where each item has been decremented by one.
#     result = list( map( lambda x: x-1, list_of_nums ) )
#     return result

# print( decrement_list( [2,3,4,5] ) )

# pull out all the inactive users
# users = [
# 	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
# 	{"username": "katie", "tweets": ["I love my cat"]},
# 	{"username": "jeff", "tweets": []},
# 	{"username": "bob123", "tweets": []},
# 	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
# 	{"username": "guitar_gal", "tweets": []}
# ]
# this is one way to do this
# count = 0
# for item in users:
#     print( item )
#     for values in item.values():
#         if values == []:
#             count += 1
# print( f"{count} users found as inactive" )  
# this is one way to do this
# using filter()
# inactive_users = len(list(filter(lambda item: item["tweets"] == [] , users)))
# print( inactive_users )
# using filter()

# using map() and filter() to pull out all the users who are inactive
# inactive_users = map(lambda inactive_username: inactive_username["username"], filter(lambda no_tweets: not no_tweets["tweets"], users))
# print( list(inactive_users) )

# Define extremes below:
# def extremes( lst ):
#     # It should return a tuple containing the minimum and maximum elements.
#     return [ min( lst ), max( lst ) ]
# def max_magnitude( lst_of_nums ):
#     # It should return the magnitude of the number with the largest magnitude (the number that is furthest 
#     # away from zero).
#     # example: max_magnitude([300, 20, -900])   #900
#     # max_magnitude([10, 11, 12])   #12
#     # max_magnitude([-5, -1, -89])   #89
    
#     # make all the items inside the list as positive numbers using abs() and store them in a list
#     pos_nums_lst = []
#     for nums in lst_of_nums:
#         pos_nums_lst.append(abs(nums))
#     return max(pos_nums_lst)
        
# print(max_magnitude( [1, 2, 3, -55] ))

# ==========================================================================================
# sum_even_values
# Write a function called sum_even_values. This function should accept a variable number of 
# arguments and return the sum of all the arguments that are divisible by 2. If there are no 
# numbers divisible by 2, the function should return 0.  To be clear, it accepts all the 
# numbers as individual arguments!

# sum_even_values(1,2,3,4,5,6) # 12
# sum_even_values(4,2,1,10) # 16
# sum_even_values(1) # 0
# ==========================================================================================
'''
sum_even_values(1,2,3,4,5,6) # 12
sum_even_values(4,2,1,10) # 16
sum_even_values(1) # 0
'''

# define sum_even_values

# def sum_even_values( *args ):
#     # This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2
#     # variable to store  the sum of all the arguments that are divisible by 2
#     result = 0
#     # iterate over args(tuples) and check if the arguments were even or not
#     for i in args:
#         if i % 2 == 0:
#             result += i
#     return result

# print(sum_even_values( 1, 2, 4, 5 ))

# ==========================================================================================
# sum_floats
# Write a function called sum_floats. 
# This function should accept a variable number of arguments. 
# The function should return the sum of all the parameters that are floats. 
# If there are no floats the function should return 0
# ==========================================================================================

'''
sum_floats(1.5, 2.4, 'awesome', [], 1) # 3.9
sum_floats(1,2,3,4,5) # 0
'''

# def sum_floats( *args ):
#     return sum( float_nums for float_nums in args if type(float_nums) == float ) 

# print( sum_floats( "munna", [], 2, 2.1, 4, 2.1 ) )

# ==========================================================================================
# Interleaving Strings (kind of tough!)
# This challenge is a bit more involved than the others in this section.  Do not worry if you can't get it!
# Write a function interleave  that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. For example:
# interleave('hi','ha')    # 'hhia'
# interleave('aaa', 'zzz')  # 'azazaz'
# interleave('lzr','iad') #  'lizard'
#  This might seem like an easy task using zip , but in fact there are a couple intermediate steps to go from zip  back to a single string.  If you need help, I've written up a basic walkthrough of the steps:
# suppose we call interleave('hi', 'no')  
# zip  the two strings together, giving you a list of tuples (once you convert from the default zip_object) -  [('h','n'), ('i','o')]  
# For each of the tuples in the list, join them together using "".join  resulting in ['hn', 'io']  - Easiest if you use a list comp.  You need to join EACH tuple.
# Finally, join the items in the list together using "".join  again resulting in 'hnio'  
# ==========================================================================================
# def interleave( str1, str2 ):
#     # It should return a new string containing the 2 strings interwoven or zipped together. For example:
#     # interleave('hi','ha')    # 'hhia'
#     # interleave('aaa', 'zzz')  # 'azazaz'
#     # interleave('lzr','iad') #  'lizard'
#     return "".join(i+j for i, j in zip( str1, str2 ))

# print( interleave('hi','ha'))

# ==========================================================================================
# triple_and_filter
# Write a function called triple_and_filter. 
# This function should accept a list of numbers, filter out every number that is not evenly 
# divisible by 4 (i.e., filter out numbers that do not divide by 4 with a remainder of zero), 
# and return a new list where every remaining number is tripled.
# ==========================================================================================
'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''
# def triple_and_filter( lst_of_nums ):
#     # The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
#     # filter(function, iterable)
#     # return [ for filtered in filter( lambda nums: num % 4 != 0, lst_of_nums )]
#     return [ filtered_nums*3 for filtered_nums in filter( lambda nums: nums % 4 == 0, lst_of_nums ) ]


# print( triple_and_filter([1,2,3,4]) )
# ==========================================================================================
# extract_full_name
# Write a function called extract_full_name. 
# This function should accept a list of dictionaries and return a new list of strings with 
# the first and last name keys in each dictionary concatenated.
# ==========================================================================================

'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name( list_of_dicts ):
    # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

    # Syntax
    # map(function, iterables)
    # extract the keys = "first" and vlaues = 'last'
    return list( map( lambda items: items['first'] + " " + items['last'], list_of_dicts ) )

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))