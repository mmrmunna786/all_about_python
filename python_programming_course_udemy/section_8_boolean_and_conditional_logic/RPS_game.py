# rock beats scissors but not paper
# paper beats rock but not scissors
# scissors beats paper but not rock
from random import choice

# prompt user for input and save the input all in lowercase in a variable
player_input = input("Please enter your move: ").lower()

# show the user what has been inputted
print( f"Player move: { player_input }" )

# get the random move from the computer
options = [ "rock", "paper", "scissors" ]
computer_input = choice( options )

# show the user what move computer has made
print( f"Computer move: { computer_input }" )

# determine the winner
if player_input == computer_input:
    print( "It's a tie!!" )
else:
    if player_input == "rock":
        if computer_input == "scissors":
            print( "Player wins!!" )
        else:
            print( "Computer wins!!" )
    elif player_input == "paper":
        if computer_input == "rock":
            print( "Player wins!!" )
        else:
            print( "Computer wins!!" )
    else: # scissors
        if computer_input == "paper":
            print( "Player wins!!" )
        else:
            print( "Computer wins!!" )
