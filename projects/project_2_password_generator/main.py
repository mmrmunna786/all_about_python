# Author: Munna
# Date: 18/07/2026
'''
Description:
The password generator conditions for random password generation are as follows:
1. 8 characters long
2. 1 upper character
3. 1 lower character
4. 1 numeric digit
5. 1 special symbol
The password generator conditions for readable password generation are as follows:
1. word + symbol + number
'''
from random import choice
# define the character sets for password generation
lower_chars = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ] 
upper_chars = [ ch.upper() for ch in lower_chars ]
digits = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
special_symbols = [ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
                '[', ']', '{', '}', '|', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/' ]
# -----------------------------------------------------------------------------------------
# print the welcome message
print( "----------------------------------" )
print( "Welcome to the Password Generator!" )
print( "----------------------------------" )
# take the user input for random password generation or readable password generation
user_input = input( "Enter 1 for random password generation or 2 for readable password generation: " )

# check for valid input
if user_input not in [ "1", "2" ]:
    print( "Invalid input. Please enter 1 or 2." )
    exit()
else:
    print( "Generating password..." )

generated_password = "" # variable to store the generated password
if user_input == "1":
    for _ in range(8):
        # take a random element from each of the list above and add it to the random_password variable
        generated_password += choice( lower_chars + upper_chars + digits + special_symbols )
    print( f"\nGenerated random password: {generated_password}" )
elif user_input == "2":
    # Implement readable password generation logic here
    wordlist = []
    with open( "random_text_from_wikipedia.txt", "r" ) as file:
        lines = file.readlines()
        # print( len(lines) )
        for line in lines:
            # print( line )
            words = line.split()
            # print( words )
            for word in words:
                # print( list( word ) )
                # clean the word by removing any special characters or punctuation
                clean_word = ''.join( ch for ch in word if ch.isalpha() ) # keeps only alphabetic characters
                # only add words taht are longer than 5 characters to the wordlist
                if len( clean_word ) > 5:
                    wordlist.append( clean_word.capitalize() ) # capitalize the first letter of the word
    # print( "\n\n", wordlist, "\n\n", len(wordlist) )
    word = choice( wordlist )
    symbol = choice( special_symbols )
    digit = choice( digits ) + choice( digits )
    generated_password = word + symbol + digit
    print( f"\nGenerated readable password: {generated_password}" )
