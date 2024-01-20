'''
Name: Charlie Man
Date: 1/4/24
blackjack.py

Description: This is the main program file to run the blackjack game.
'''


from cards import Card, Deck, Hand, Chips
from utils import hit, hit_or_stand, show_some, show_all, player_busts,\
player_wins, dealer_busts, dealer_wins, push


chips = Chips()

while True:
    print("Welcome to Blackjack!")
    print("Your chips total is {}.".format(chips.total))
    
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    
    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    
    chips.take_bet()
    
    print('\n')
    show_some(player,dealer)
    
    playing = True
    
    while playing:
        
        print('\n')
        hit_or_stand(deck,player)
        
        print('\n')
        show_some(player,dealer)
        print('\n')
        
        if player.value > 21:
            player_busts(player,dealer,chips)
            break
            
    if player.value <= 21 and player.value != 0:
        while dealer.value < 17:
            hit(deck,dealer)

        print('\n')
        show_all(player,dealer)
        print('\n')

        if dealer.value > 21:
            dealer_busts(player,dealer,chips)

        elif player.value > dealer.value:
            player_wins(player,dealer,chips)

        elif dealer.value > player.value:
            dealer_wins(player,dealer,chips)

        elif player.value == dealer.value:
            push(player,dealer,chips)
        
    print("Your chips total is {}.".format(chips.total))
        
    play_again = input("Would you like to play again? Enter 'y' for yes or "
                       "'n' for no: ")
        
    while play_again != "y" and play_again != "n":
        play_again = input("Sorry, I don't understand. Would you like to play "
                           "again? Enter 'y' for yes or 'n' for no: ")
            
    if play_again == "n":
        print("Thank you for playing!")
        break
    
    print('\n')