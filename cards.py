'''
Name: Charlie Man
Date: 1/4/24
cards.py

Description: This file contains the Card, Deck, Hand, and Chips classes. Each
class consists of various methods to be used when running the blackjack.py
program.
'''


import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
         'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10,
          'Ace':11}


'''
Card
Description: The Card class contains a constructor and a print module.
'''
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


'''
Deck
Description: The Deck class contains a constructor, a print module, and two
functions to shuffle the deck and deal a card.
'''
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_str = ""
        for card in self.deck:
            deck_str += '\n' + card.__str__()
        return "The deck has: " + deck_str
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()


'''
Hand
Description: The Hand class contains a constructor and two functions to add a
card to the hand and adjust for aces in the hand.
'''
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1
            self.adjust_for_ace()
        else:
            self.value += card.value
        
    def adjust_for_ace(self):
        ace_counter = self.aces
        if self.value + 11 <= 21:
            self.value += 11
            ace_counter -= 1
        else:
            self.value += 1
            ace_counter -= 1


'''
Chips
Description: The Chips class contains a constructor and three functions to 1)
accept input for the user's bet, 2) to update the chips if the user wins, and
3) to update the chips if the user loses.
'''
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        self.bet = 0
        
    def lose_bet(self):
        self.total -= self.bet
        if self.total < 0:
            self.total = 0
        self.bet = 0
        
    def take_bet(self):
        while True:
            try:
                self.bet = int(input("Please enter your bet amount: "))
                while self.bet > self.total or self.bet < 0:
                    self.bet = int(input("The bet amount you entered is "
                                         "invalid. You have an available "
                                         "balance of {}. Please try again: "\
                                         .format(self.total)))
                break
            except:
                print("Invalid amount! Please try again.")
                continue
