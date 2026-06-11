# print the tiltle with asci art
from pyfiglet import Figlet
from termcolor import colored, COLORS
from random import choice


def print_colored_message(message, color):
    # check if the user text message has been entered  or not
    if message == "":
        message = "Dad Joke 3000"
    # check if the user color has been entered  or not
    if color == "":
        color = choice(list(COLORS.keys()))

    # now print the user message in the color they want
    # select the font for the message
    f = Figlet(font="big")
    # render the message in the selected font and color
    colored_message = colored(f.renderText(message), color)
    # print the colored message
    print(colored_message)


# pyfiglet usage example:
"""
from pyfiglet import Figlet
        f = Figlet(font='slant')
        print(f.renderText('text to render'))
"""
# termcolor usage example:
"""
import sys
from termcolor import colored, cprint
text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")
"""

# ask user for message
# print( "what message do you want to print?" )
# user_message = str( input( "Enter the message here \U0001F449: " ) )
# # ask user for color
# print( "what color do you want to print in?" )
# user_color = str( input( "Enter the color here \U0001F449: " ) )

print_colored_message("", "")

# ask user to input a topic and save it to a variable
user_input = input("\n\nLet me tell you a joke! Give me a topic: ")

# pass this user input as input parameter in the URL to get the joke as a response
import requests

url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, params={"term": f"{user_input}"}, headers={"Accept": "application/json"}
)

json_data = res.json()
# store the number of jokes in a variable
no_of_jokes = len(json_data["results"])

# print(json_data["results"])
# print the number of jokes found for the user input topic
if no_of_jokes == 0:
    print( f"Sorry I don't have any jokes about {user_input}" )
else:
    print(f"Found {no_of_jokes} jokes about {user_input}. Here's one for you!")
    # print a random joke from the results
    from random import randint
    rand_num = randint(0, no_of_jokes-1)
    # check if generated random number is 0, if so then set rand_num
    # if rand_num == 0:
    #     rand_num = 1
    print(json_data["results"][rand_num]["joke"])



