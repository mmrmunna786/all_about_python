# Author: Munna
# Date: 12/07/2026

'''
Write a function called once. This function accepts a function and returns a new function 
that can only be invoked once. If the function is invoked more than once, it should return 
None. Hint you will need to define a new function inside of your once function and return 
that function. You can add properties to your inner function to see if it has run already.

For example:
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None

algorithm:
1. Define a function called once that accepts a function (func):
   a. Create a variable called "is_called" and set it to False
   b. Define an inner function that accepts *args:
      i. Check if is_called is False
      ii. If False:
          - Set is_called to True
          - Call func with the arguments and return the result
      iii. If True:
          - Return None
   c. Return the inner function
'''
def once( func ):
    func.is_called = False
    def inner_func(*args):
        if not(func.is_called):
            func.is_called = True
            return func(*args)
        else:
            return None
    return inner_func

def add(a,b):
    return a+b

oneAddition = once(add)

print(oneAddition(2,2)) # 4
print(oneAddition(2,2)) # None
print(oneAddition(12,200)) # None