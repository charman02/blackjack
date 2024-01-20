'''
Name: Charlie Man
Date: 1/4/24
utils.py

Description: This is a separate module for utility functions, which are used in
the main program file.
'''


playing = True


'''
DOCSTRING
Input: Deck, hand
Output: None
'''
def hit(deck,hand):
    hand.add_card(deck.deal())


'''
DOCSTRING
Input: Deck, player's hand
Output: None
'''
def hit_or_stand(deck,hand):
    global playing
    move = input("Would you like to hit or stand?")
    while move != "hit" and move != "stand":
        move = input("Sorry, I don't understand. Please enter 'hit' or "
                     "'stand': ")
    if move == "hit":
        hit(deck,hand)
    else:
        playing = False


'''
DOCSTRING
Input: Player and dealer's hands
Output: Dealer's hand (first card hidden) and player's hand/value
'''
def show_some(player,dealer):
    print("Dealer:")
    print("First card hidden!",*dealer.cards[1:],sep='\n')
    print(f"\nPlayer: {player.value}",*player.cards,sep='\n')
    

'''
DOCSTRING
Input: Player and dealer's hands
Output: Player and dealer's hands/values
'''
def show_all(player,dealer):
    print(f"Dealer: {dealer.value}",*dealer.cards,sep='\n')
    print(f"\nPlayer: {player.value}",*player.cards,sep='\n')


'''
DOCSTRING
Input: Player's hand, dealer's hand, player's chips
Output: Message to console indicating that player busted
'''
def player_busts(player,dealer,chips):
    print("Bust! You lost.")
    player.cards = []
    player.value = 0
    player.aces = 0
    dealer.cards = []
    dealer.value = 0
    dealer.aces = 0
    chips.lose_bet()


'''
DOCSTRING
Input: Player's hand, dealer's hand, player's chips
Output: Message to console indicating that player won
'''   
def player_wins(player,dealer,chips):
    print("You won!")
    player.cards = []
    player.value = 0
    player.aces = 0
    dealer.cards = []
    dealer.value = 0
    dealer.aces = 0
    chips.win_bet()


'''
DOCSTRING
Input: Player's hand, dealer's hand, player's chips
Output: Message to console indicating that dealer busted
'''
def dealer_busts(player,dealer,chips):
    print("Dealer busted! You won!")
    player.cards = []
    player.value = 0
    player.aces = 0
    dealer.cards = []
    dealer.value = 0
    dealer.aces = 0
    chips.win_bet()


'''
DOCSTRING
Input: Player's hand, dealer's hand, player's chips
Output: Message to console indicating that dealer won
'''
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    player.cards = []
    player.value = 0
    player.aces = 0
    dealer.cards = []
    dealer.value = 0
    dealer.aces = 0
    chips.lose_bet()


'''
DOCSTRING
Input: Player's hand, dealer's hand, player's chips
Output: Message to console indicating push result
'''
def push(player,dealer,chips):
    print("Push! It's a tie.")
    player.cards = []
    player.value = 0
    player.aces = 0
    dealer.cards = []
    dealer.value = 0
    dealer.aces = 0
    chips.bet = 0
