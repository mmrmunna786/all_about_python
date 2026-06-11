#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

# result = []

# def generate_evens():
#     for nums in range( 1, 50 ):
#         if nums % 2 == 0:
#             result.append( nums )
#     return result
# print( generate_evens() )

# '''Yell Function Exercise
# Implement a function yell  which accepts a single string argument.  
# It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  
# For example:

# yell("go away")   # "GO AWAY!"

# yell("leave me alone")   # "LEAVE ME ALONE!"

# You do not need to call the function to pass the tests.'''
# def yell( a_string ):
    
#     return a_string.upper() + "!"

# print( yell( "mo" ) )

'''Write a function called speak  that accepts a single parameter, animal.  

If animal is "pig", it should return "oink". 
If animal is "duck", it should return "quack".  
If animal is "cat", it should return "meow"
If animal is "dog", it should return "woof"
If animal is anything else, it should return "?"
If no animal is specified, it should default to "dog"


speak()  # "woof"
speak("pig")  # "oink"
speak("duck")  # "quack"
speak("cat")  # "meow"
speak("dog")  # "woof"
speak("banana")  # "?"
'''

# # Define speak below:
# def speak( animal="dog" ):
#     if animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     elif animal == "dog":
#         return "woof"
#     else:
#         return "?"
    
# print( speak("banana") )

# name = "Rusty"

# def greet():
#     global name 
#     name = "Rusty steele"
#     # print( name )
#     return name
    
# print(greet())


