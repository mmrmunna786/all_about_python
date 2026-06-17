"""
Web scraping project
Introduction
In this project you'll be building a quotes guessing game. When run, your program will scrape a website for a collection of quotes.
Pick one at random and display it. The player will have four chances to guess who said the quote.
After every wrong guess they'll get a hint about the author's identity.

Requirements
    1. Create a file called `scraping_project.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
    2. You can use `bs4` and `requests` to get the data. For each quote you should grab the text of the quote, the name of the person
       who said the quote, and the href of the link to the person's bio. Store all of this information in a list.
    3. Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
    4. After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying
       the author, the player loses and the game ends. If the player correctly identifies the author, the player wins!
    5. After every incorrect guess, the player receives a hint about the author.
        a. For the first hint, make another request to the author's bio page (this is why we originally scrape this data), and tell the
           player the author's birth date and location.
        b. The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's
           last name, the number of letters in one of the names, etc.
    6. When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote.
       If no, the program is complete.
Good luck!
"""

from bs4 import BeautifulSoup  # library for web scraping
import requests # library for making http requests
from random import choice 

base_url = "http://quotes.toscrape.com" 
next_button_url = "/page/1"
all_quotes = [] # list to store all quotes, author-name, author-bio

while next_button_url: # while there is next button available in the web page
   url = f"{base_url}{next_button_url}" # concatenate the base url with the page number
   print( f"Scraping {url}" ) # debug print statement
   response = requests.get(url).text # get the response as text
   # find all the html tag with class="quote" and store it in a list called quotes
   soup = BeautifulSoup(response, "html.parser") # parse the response as html
   quotes = soup.find_all(class_="quote")  # returns a list containing all the html tags which has class equal to "quote"
   # For each quote you should grab the text of the quote,
   for quote in quotes:
      # print( quote.find( class_="text" ).get_text() )  # returns the inner text of each element in the list
      # Store all of this information in a list of dictionaries.
      all_quotes.append({
               "quote_text": quote.find(class_="text").get_text(),  # get the quote text
               "author_name": quote.find(class_="author").get_text(),  # get the author name
               "author_bio_link": quote.find( "a" )["href"]
                       })
   # find the next button on the web page
   next_button = soup.find( class_='next' )
   # find the immidiate next anchor tag containing the url if next button exists on the web page
   next_button_url = next_button.find( "a" )["href"] if next_button else None
# print( all_quotes )

def play_again():
   play_again = input( "Would you like to play it again? (y/n): " ).lower()
   while play_again == "":
      print( "You have not entered anything." )
      play_again = input( "Would you like to play it again? (y/n): " ).lower()
      if play_again != "":
         break
   if play_again == "y":
      return play_game()
   else:
      print("Thanks for playing!!")
      return False
# 3. Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
def play_game():
   quote = choice( all_quotes ) # take a random quote from the scraped data in the list
   remaining_guesses = 4 # varibale for guess counting
   print( f"Here's a quote: {quote['quote_text']}" ) # display a quote to the user 
   print( quote[ "author_name" ] ) # debugging purpose and will be removed later
   guess = '' # varibale to store the guess text
   while guess.lower() != quote[ "author_name" ].lower() and remaining_guesses > 0:
      guess = input( f"Guess remaining {remaining_guesses}, Who said this quote? \U0001F449 " ) # prompt the user for guessed input
      if guess.lower() == quote['author_name'].lower():
         print( "You got it right!!!" )
         if play_again() == False:
            break
      remaining_guesses -= 1 # decrement the guess count by 1
      if remaining_guesses == 3: # of the user has made 2 wrong guesses then give then a hint about the author 
         res = requests.get( f"{base_url}{quote['author_bio_link']}" )
         soup = BeautifulSoup( res.text, "html.parser" )
         author_born_date = soup.find( class_="author-born-date" ).get_text()
         author_born_location = soup.find( class_="author-born-location" ).get_text()
         print( f"Here's a hint: The author was born on {author_born_date} {author_born_location}" )
      elif remaining_guesses == 2:
         print( f"Here's another hint: The author's first name starts with {quote[ 'author_name' ][0]}" )
      elif remaining_guesses == 1:
         last_name_initial = quote[ 'author_name' ].split()[1][0]
         print( f"Here's another hint: The author's last name starts with {last_name_initial}" )
      else:
         print( f"Sorry ran out of guesses. The answer was {quote['author_name']}" )
         if play_again() == False:
            break
play_game()
print( "after while loop" )


   