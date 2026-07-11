# Author: Munna
# Date: 11/07/2026

'''
Write a function called three_odd_numbers, which accepts a list of numbers and 
returns True  if any three consecutive numbers sum to an odd number.

For example:
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''
'''
algorithm:
1. Check every group of 3 consecutive numbers
2. Add the 3 numbers in that group
3. If the sum is odd, return True
4. If no group works, return False
'''

def three_odd_numbers(in_lst):
    # 1. Check every group of 3 consecutive numbers
    for i in range(len(in_lst) - 2):
        # 2. Add the 3 numbers in that group
        total = in_lst[i] + in_lst[i + 1] + in_lst[i + 2]

        # 3. If the sum is odd, return True
        if total % 2 != 0:
            return True

    # 4. If no group works, return False
    return False

print(three_odd_numbers([1,2,3,4,5])) # True
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0])) # True
print(three_odd_numbers([5,2,1])) # False
print(three_odd_numbers([1,2,3,3,2])) # False