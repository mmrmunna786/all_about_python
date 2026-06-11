# loop through the numbers 1 to 20
# => for 4 and 13, print "Unlucky!"
# => for even numbers, print "Even"
# => for odd numbers, print "Odd"

given_range = range( 1, 20+1 )
for number in given_range:
    if number == 4 or number == 13:
        print( f"The number is {number} therefore, \"UNLUCKY\"" )
    else:
        if number % 2 == 0: 
            print( f"The number {number} is \"Even\"" )
        else:
            print( f"The number {number} is \"Odd\"" )