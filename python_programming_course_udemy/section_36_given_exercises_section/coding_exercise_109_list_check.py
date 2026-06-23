# Author: Munna
# Date: 22/06/2026

'''
list_check
Write a function called list_check, which accepts a list and returns True if 
each value in the list is a list. Otherwise the function should return False.

Example input output:
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''
# loop over all the items in the list, if any item isnt't a list then return false
def list_check( in_lst ):
    result = False
    for val in in_lst:
        if type(val) != list:
            return False
        result = True
    return result
print( list_check([[],[1],[2,3], (1,2)]) )

# another simple solution
def list_check( in_lst ):
    return all( type( item ) == list for item in in_lst) 

print( list_check([[],[1],[2,3], (1,2)]) )
print( list_check([1, True, [],[1],[2,3]]) )
print( list_check([[],[1],[2,3]]) )