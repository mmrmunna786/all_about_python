# Author: Munna
# Date: 06/07/2026

'''
Write a function called truncate that will shorten a string to a specified length, and 
add "..." to the end.  Given a string and a number n, truncate the string to a shorter 
string containing at most n characters. For example, truncate("long string", 5)  should 
return a 5 character truncated version of "long string".  If the string gets truncated, 
the truncated return string should have a "..." at the end. Because of this, the smallest 
number passed in as a second argument should be 3. 

For example:
truncate("Hello World", 6) # "Hel..."   
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
'''
def truncate( in_str, in_num ):
    # the smallest number passed in as a second argument should be 3.
    if ( in_num < 3 ):
        return "Truncation must be at least 3 characters"
    if ( in_num > len( in_str ) + 2 ):
        return in_str
    return in_str[ :in_num - 3 ] + "..."

print(truncate("Hello World", 13)) # "Hel..."   
print(truncate("Woah", 4)) # "W..."
print(truncate("Woah", 3)) # "..."
print(truncate("Problem solving is the best!", 10)) # "Problem..."
print(truncate("Super cool", 2)) # "Truncation must be at least 3 characters."