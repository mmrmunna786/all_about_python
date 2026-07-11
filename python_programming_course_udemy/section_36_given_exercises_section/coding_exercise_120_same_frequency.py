# Author: Munna
# Date: 06/07/2026

'''
Write a function called same_frequency which accepts two numbers and returns True if they contain 
the same frequency of digits. Otherwise, it returns False.

For example:
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(num1, num2):
    # convert the numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    # check if the lengths of the two strings are equal
    if len(str_num1) != len(str_num2):
        return False
    # create a dictionary to store the frequency of digits in num1
    freq_dict = {}
    for digit in str_num1:
        if digit in freq_dict:
            freq_dict[digit] += 1
        else:
            freq_dict[digit] = 1
    # check if the frequency of digits in num2 matches that of num1
    for digit in str_num2:
        if digit not in freq_dict or freq_dict[digit] == 0:
            return False
        freq_dict[digit] -= 1
    return True

print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True