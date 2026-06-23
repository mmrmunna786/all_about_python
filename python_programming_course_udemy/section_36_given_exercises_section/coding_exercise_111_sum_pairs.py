# Author: Munna
# Date: 23/06/2026

'''
sum_pairs
Write a function called sum_pairs which accepts a list and a number and returns 
the first pair of numbers that sum to the number passed to the function.

Example input output:
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

# def sum_pairs( in_lst, num ):
#     # loop through the entire length of the given list
#     for idx in range( 0, len( in_lst ) ):
#         # check if the list is empty or not, if it is then return an empty list
#         if len(in_lst) == 0:
#             return []
#         else: 
#             # check if the index value is greater than the length itself or not
#             if idx == len( in_lst ) - 1:
#                 break
#             else:
#                 # take 1st item and 2nd item in the list using indexing and sum them
#                 summed_item = in_lst[ idx ] + in_lst[ idx + 1 ]
#                 # if summed_item is equal to the num(target) then return those two values in a list
#                 if summed_item == num:
#                     return [ in_lst[ idx ], in_lst[ idx + 1 ] ]
#                 else:
#                     return []
# print( sum_pairs([11,20,4,2,1,5], 100) )

# given solution
# ==============================================================
# def sum_pairs(ints, s):
#     already_visited = set()
#     print( already_visited )
#     for i in ints:
#         difference = s - i
#         if difference in already_visited:
#             return [difference, i]
#         already_visited.add(i)
#     return [] 

# # print(sum_pairs([4,2,10,5,1], 6)) # [4,2]
# # print(sum_pairs([11,20,4,2,1,5], 100)) # []
# ==============================================================
