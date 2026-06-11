'''*args Exercise: The Purple Test
Define a function contains_purple  that accepts any number of arguments.  It should return True  if any of the arguments are "purple" (all lowercase). Otherwise, it should return False .  For example:

contains_purple(25, "purple")   #True

contains_purple("green", False, 37, "blue", "hello world")   #False

contains_purple("purple")   #True

contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")   #True

contains_purple(1,2,3)  #False

Always remember, purple is the best color on this earth.  All hail purple.'''

# def contains_purple( *args ):
#     for i in range(0, len(args)):
#         if args[i] == "purple":
#             return True
#         return False
    
# print( contains_purple( 1, 2, "purple" ) ) # should return purple

# def fav_colors( **kwargs ):
#     print( kwargs )
    
# fav_colors( colt="purple", ruby="red" )

'''
**kwargs Exercise
Note: for this exercise, make use of **kwargs.  No default parameters allowed!

Write a function called combine_words  which accepts a single string called word and any number of additional key word arguments.  If a prefix is provided, return the prefix followed by the word.  If a suffix is provided, return the word followed by the suffix.  If neither is provided, just return the word.  It might sound confusing, but the examples should make this a lot clearer!

combine_words("child")  #'child'

combine_words("child", prefix="man")  #'manchild'

combine_words("child", suffix="ish")  #'childish'

combine_words("work", suffix="er")  #'worker'

combine_words("work", prefix="home")  #'homework'
'''
# # Define combine_words below:
# def combine_words( word, **kwargs ):
#     # If neither is provided, just return the word.
#     if not kwargs:
#         return word
#     else:
#         #  If a prefix is provided, return the prefix followed by the word.
#         for key, value in kwargs.items():
#             if key == "prefix":
#                 return value+word
#         # If a suffix is provided, return the word followed by the suffix.
#             return word+value
# print( combine_words( "child" ) )
# print( combine_words( "child", prefix="man" ) )
# print( combine_words( "child", suffix="ish" ) )
# print( combine_words( "child", suffix="er" ) )
# print( combine_words( "child", prefix="home" ) )

# n = int(input())

# if n >= 1 and n <= 20:
#     for i in range( 0, n ):
#         if i == 0:
#             print( 0 )
#         else:
#             print( i ** 2 ) 

# def is_leap(year):
#     leap = False
    
    # Write your logic here
#     if year in range( 1900, (10**5)+1 ):
#         if year % 4 == 0:
#             if year % 100 == 0:
#                 if year % 400 == 0:
#                     return True
#                 else:
#                     return False      
#             return True
#         else:
#             return leap

# year = int( input() )
# print( is_leap( year ) )

# n = int(input())
    
# for i in range( 1, n+1 ):
#     print( i, end="" )
    
# def sum_all_values( *args ):
#     # print( args )
#     total = 0
#     for num in args:
#         total += num
#     print( total )

# nums = ( 1,2,3,4,5 )
# sum_all_values( *nums )

# def calculate( **kwargs ):
#     # in the case of message = True, meaning any message has been passed as string
#     if "message" in kwargs:
#         if "add" in kwargs.values():
#             if False in kwargs.values():
#                 return f"You just added {first + last}"
#             # else:
#             #     return (f"You just added " {float(first + last)})
#         elif "subtract" in kwargs.values():
#             if False in kwargs.values():
#                 return f"You just subtracted {first - last}"
#             # else:
#             #     return (f"You just subtracted " {float(first - last)})  
#         elif "multiply" in kwargs.values():
#             if False in kwargs.values():
#                 return f"You just multiplied {first * last}"
#             # else:
#             #     return (f"You just multiplied " {float(first * last)})
#         elif "divide" in kwargs.values():
#             if False in kwargs.values():
#                 return f"You just divided {first / last}"
#             # else:
#             #     return (f"You just multiplied " {float(first / last)})
#     else:
#         if "add" in kwargs.values():
#             if True in kwargs.values():
#                 return f"The result is {float(first + last)}"
#         elif "subtract" in kwargs.values():
#             if True in kwargs.values():
#                 return f"The result is {float(first - last)}"
#         elif "multiply" in kwargs.values():
#             if True in kwargs.values():
#                 return f"The result is {float(first * last)}"
#         elif "divide" in kwargs.values():
#             if True in kwargs.values():
#                 return f"The result is {float(first / last)}"
def calculate( **kwargs ):
    operation_looup_and_compute = { # this will lookup the values in 
                                   # "first" and "second" arguments 
                                   # and compute by the "operation" argument
        "add": kwargs.get( "first", 0 ) + kwargs.get( "second", 0 ),
        "subtract": kwargs.get( "first", 0 ) - kwargs.get( "second", 0 ),
        "multiply": kwargs.get( "first", 0 ) * kwargs.get( "second", 0 ),
        "divide": kwargs.get( "first", 0 ) / kwargs.get( "second", 0 ),
    }
    
    is_float = kwargs.get( "make_float", False )
    computed_value_by_operation = operation_looup_and_compute[ kwargs.get( "operation", "" ) ]
    
    if is_float:
        final = f"{kwargs.get( "message", "The result is" )} {float( computed_value_by_operation )}"
    else:
        final = f"{kwargs.get( "message", "The result is" )} {int( computed_value_by_operation )}"
    return final

print( calculate(make_float=True, operation='divide', first=3.5, second=5) )