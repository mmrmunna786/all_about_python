# repeat everything until the user says "stop copying me"

# take the user input
user_input = input().lower()

# print what's been inputted repeatedly until "stop copying me" is inputted
while user_input != "stop copying me":
    print( user_input )
    # take the user input
    user_input = input().lower()
    
# exit out message
print( "Ugh fine you've won" )
    
