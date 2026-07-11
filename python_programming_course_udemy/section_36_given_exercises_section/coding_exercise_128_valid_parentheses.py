# Author: Munna
# Date: 11/07/2026

'''
Write a function called valid_parentheses that takes a string of parentheses, and determines if the 
order of the parentheses is valid. valid_parentheses should return true if the string is valid, and 
false if it's invalid.

For example:
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses( in_str ):
    count = 0 # store the number of pairs(left and right bracket) of the paratheses
    i = 0 # iteration counter
    # while the iteration counter is less than length of the input string, check the index of the input 
    # string corresponds to ")" or "(", if index corresponds to "(" then increment count by 1, if index
    # corresponds to ")" then decrement count by 1.
    while i < len( in_str ):
        if in_str[ i ] == "(":
            count += 1
        if in_str[ i ] == ")":
            count -= 1
        if count < 0: # this means that there are more ")" than the pairs or "(" so return false because invalid parentheses
            return False
        i += 1
    return count == 0 # this means that if the number of "(" and ")" are equal then count will be equal to zero and will return True
                      # otherwise it will return False   

print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False