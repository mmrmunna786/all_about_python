"""
OOP Exercise
Introduction
Your goal in this exercise is to implement two classes, Card  and Deck .

Specifications
Card
1. Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
2. Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
3. Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
"""

"""
Deck 
1. Each instance of Deck should have a cards attribute with all 52 possible instances of Card .
2. Deck  should have an instance method called count which returns a count of how many cards remain in the deck.
3. Deck's __repr__ method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
4. Deck  should have an instance method called _deal which accepts a number and removes at most that many cards from the end of the deck 
(it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should 
return a ValueError with the message "All cards have been dealt".
5. Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, 
this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
6. Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that 
single card.
7. Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from 
the deck and return that list of cards.
"""
from random import shuffle


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{ self.value } of { self.suit }"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        # self.cards = []
        # for suit in suits:
        #     for value in values:
        #         self.cards.append( Card( value, suit ) )
        self.cards = [
            Card(value, suit) for suit in suits for value in values
        ]  # using list comprehension
        # print( self.cards )

    def __repr__(self):
        return f"Deck of { self.count() } cards"  # e.g. "Deck of 52 cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        current_no_of_cards = self.count()  # current no. of cards left in the deck
        no_of_cards_to_be_removed = min(
            [current_no_of_cards, num]
        )  # smallest number of cards to be removed between input and current_no_of_cards
        if (
            current_no_of_cards <= 0
        ):  # if no. of cards in the deck is 0 or less then raise an error
            raise ValueError("All cards have been delt")
        cards = self.cards[
            -no_of_cards_to_be_removed:
        ]  # remove the desired no. of cards from the end of the deck
        self.cards = self.cards[
            :-no_of_cards_to_be_removed
        ]  # update the deck after removal of cards
        return cards  # return the removed cards for dealing hand

    def deal_card(self):
        return self._deal(1)[
            0
        ]  # this ([0]) will give a single card instead of a list with a single card in it.

    def deal_hand(self, no_of_cards_to_deal):
        return self._deal(
            no_of_cards_to_deal
        )  # this will remove and return the no. of cards specified in the num variable to deal the hands.

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards


"""
Deck should have an instance method called deal_card which uses the _deal method to deal a single card from the deck and return that 
single card.

Deck should have an instance method called deal_hand which accepts a number and uses the _deal method to deal a list of cards from 
the deck and return that list of cards.

Deck should have an instance method called shuffle which will shuffle a full deck of cards. If there are cards missing from the deck, 
this method should raise a ValueError with the message "Only full decks can be shuffled". Shuffle should return the shuffled deck.
"""


def _deal( self, num ): # single underscore indicates that this is a "private" method, meaning it should not be used outside of the class
    current_no_of_cards = self.count()
    if len( self.cards ) <= 0:
        return ValueError( "All cards have been dealt" )
    else:
        if current_no_of_cards > num:
            for i in range( 0, num ):
                self.cards.pop()
        else:
            for i in range( 0, current_no_of_cards ):
                self.cards.pop()


d = Deck()
d.deal_hand(5)
print(d.shuffle())
# print(d.cards)
# print( d._deal(50) )
# print( f"{d.count()} cards left" )
