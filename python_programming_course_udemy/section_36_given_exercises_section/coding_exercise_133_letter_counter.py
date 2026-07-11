# Author: Munna
# Date: 12/07/2026

'''
Write a function called letter_counter which accepts a string and returns a function. 
When the inner function is invoked it should accept a parameter which is a letter, 
and the inner function should return the number of times that letter appears. 
This inner function should be case insensitive.

For example:
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1

algorithm:
1. make the input string all lowercase 
2. make the lowercased string varibale as nonlocal i.e., global inside the function
3. make count variable 
4. loop through the input string and check if the input char exists in the input string or
    not, if it exists then increment the count varible in step 3
5. return the count varibale at the end of th eloop
'''
def letter_counter( in_str ):
    lower_in_str = in_str.lower()
    def inner_func( in_char ):
        nonlocal lower_in_str
        total = 0
        for char in lower_in_str:
            if in_char == char:
                total += 1
        return total
    return inner_func
counter2 = letter_counter('This Is Really Fun!')
print(counter2('i')) # 2
print(counter2('t')) # 1

counter = letter_counter('Amazing')
print(counter('a')) # 2
print(counter('m')) # 1