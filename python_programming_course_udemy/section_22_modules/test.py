# pyfiglet exercise:
# ASCII AR EXERCISE:
# For example, if you run the following python file: color.py, then it will ask you 
# this "what message do you want to print?" then you give you message as string
# and then it will ask you "what color do you want to print in?" then you give the color as string
# and then it will print the message in the color you want.

from pyfiglet import Figlet
from termcolor import colored, COLORS
from random import choice

def print_colored_message( message, color ):
    # check if the user text message has been entered  or not
    if message == "":
        message = "Assalamualaikum"
    # check if the user color has been entered  or not
    if color == "":
        color = choice( list( COLORS.keys() ) )
        
    # now print the user message in the color they want
    # select the font for the message
    f = Figlet(font='slant')
    # render the message in the selected font and color
    colored_message = colored( f.renderText( message ), color )
    # print the colored message
    print( colored_message )
    
# pyfiglet usage example:
'''
from pyfiglet import Figlet
        f = Figlet(font='slant')
        print(f.renderText('text to render'))
'''
# termcolor usage example:
'''
import sys
from termcolor import colored, cprint
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")
'''
    
# ask user for message
print( "what message do you want to print?" )
user_message = str( input( "Enter the message here \U0001F449: " ) )
# ask user for color
print( "what color do you want to print in?" )
user_color = str( input( "Enter the color here \U0001F449: " ) )

print_colored_message( user_message, user_color )