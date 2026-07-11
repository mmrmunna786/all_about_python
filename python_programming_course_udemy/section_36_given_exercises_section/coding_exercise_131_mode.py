# Author: Munna
# Date: 11/07/2026

'''
Write a function called mode. This function accepts a list of numbers and returns the most frequent number in the list of numbers. 
You can assume that the mode will be unique.

For example:
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''
'''
algorithm:
1. Count the frequency of each number
2. Return the number with the highest frequency
'''

def mode( in_lst ):
    count = { val: in_lst.count(val) for val in in_lst }
    return max(count, key=count.get)

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))