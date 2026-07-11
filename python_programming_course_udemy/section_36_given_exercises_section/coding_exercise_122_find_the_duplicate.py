# Author: Munna
# Date: 07/07/2026

'''
Write a function called find_the_duplicate which accepts an array of numbers containing a single 
duplicate. The function returns the number which is a duplicate or None if there are no duplicates.

For example:
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate( in_num_lst ):
    # create an empty dictionary to store the frequency of the duplicate number
    counter = {}
    # iterate over the numbers in the input list 
    for key in in_num_lst:
        if key in counter: # if that value from the list is in the cunter dict as a key then increment it
            counter[ key ] += 1
        else:
            counter[ key ] = 1 # otherwise, it means it's a new value so set it equal to 1
    for value in counter.keys():
        if counter[ value ] > 1: # if the value of the key is greater than 1, then it is a duplicate
            return int( value )
    return None
    
print(find_the_duplicate([1,2,1,4,3,12])) # 1
print(find_the_duplicate([6,1,9,5,3,4,9])) # 9
print(find_the_duplicate([2,1,3,4])) # None