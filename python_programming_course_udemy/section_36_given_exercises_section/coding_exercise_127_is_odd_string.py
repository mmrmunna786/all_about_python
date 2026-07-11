# Author: Munna
# Date: 07/07/2026

'''
Write a function called is_odd_string which returns true if sum of each character's position in the 
alphabet is odd. For example, "a" is in the first position, "b" is in the second position, and so on. 
If the sum is even, return false.  
NOTE: INDEXING STARTS AT 1.  A is position 1, NOT POSITION 0.

For example:
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string( in_str ):
    total = 0
    for char in in_str.lower(): # converting to lowercase for safety
        total += ord( char ) - 96 # 'a' = 1, 'b' = 2, etc.
    return total % 2 != 0
print(is_odd_string('a')) # True
print(is_odd_string('aaaa')) # False
print(is_odd_string('amazing')) # True
print(is_odd_string('veryfun')) # True
print(is_odd_string('veryfunny')) # False