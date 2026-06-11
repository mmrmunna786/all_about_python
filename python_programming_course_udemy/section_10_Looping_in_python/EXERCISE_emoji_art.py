''' while loop exercise: create emoji art
 print the right angle triangle using given emoji code = "\U0001f600" 
 using both a for loop and a while loop '''
 
# using for loop
user_input = input( "Please enter the number of rows: " )
for rows in range( int( user_input ) ):
    print( "\U0001f600" * ( rows+1 ) )
    
# using while loop
# take the user input and store it in a variable
user_input = input( "Please enter the number of rows: " )
# couter variable for row counting
rows = 1
while rows <= int( user_input ):
    print( "\U0001f600" * rows )
    rows += 1
    