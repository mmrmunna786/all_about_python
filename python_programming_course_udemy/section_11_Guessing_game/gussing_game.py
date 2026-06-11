from random import randint

# generate the correct number
correct_number = randint(1, 10)

# take the user input
user_input = int(input("Guess a number between 1 and 10: "))

# variable for loop breaking
keep_playing = None

# check if the user's number is greater or lower than the correct number
while True:
    if user_input > correct_number:
        print(f'your gussed number "{user_input}" is too high!!')
        user_input = int(input("Guess again: "))
    elif user_input < correct_number:
        print(f'your gussed number "{user_input}" is too low!!')
        user_input = int(input("Guess again: "))
    else:
        print(f'your gussed number "{user_input}" is correct!!')
        keep_playing = input("Do you want to play again? Enter y or n: ").lower()

        if keep_playing == "n": # if loop break variable is equal to "n" then exit out of the loop
            break
        else:
            correct_number = randint(1, 10) # reset the randomly generated correct number 
            user_input = int(input("Guess a number between 1 and 10: ")) # take the fresh user input

