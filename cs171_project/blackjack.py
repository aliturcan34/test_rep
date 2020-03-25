#Winter CS171 project
#Author: Ali Kagan Turcan
#email: akt67@drexel.edu
#Game: Blackjack


import player
import dealer
import deck
import errors

ranks = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "Ace":11,"King":10, "Queen":10,"Jack":10}
suits = ["clubs","diamonds","hearts","spades"]  

def card_value_finder(cards):
    card_sum = 0
    isAce  = False
    for card in cards:                             #(1f)function for finding the values of the cards as well as evaluating which value should ace hold.
        val = card.split()
        card_sum += ranks[val[1]]
        if val[0] == "Ace":
            isAce = True                            #(1c)checks if ace is present in the deck
    if isAce:                                     
        if card_sum > 21:
            card_sum -= 10                          #(2c)adjusts the sum if it is bigger than 21 by making the ace worth 1
    return card_sum

buying_chips_check = True

while buying_chips_check:                    #(1l)check if the inputs are valid while buying the chips
    try:
        chips = int(input("Please enter the number of chips you want to buy:\n"))
        if type(chips) == float:
            raise ValueError
        buying_chips_check = False
        print("Chips bought:",chips)
    except ValueError as v:
        print("Invalid entry! The number of chips must be an integer.")
player1 = player.Player(chips, [])

game_loop_check = True
while game_loop_check and  player1.chips>= 5:                   #(2l)the main loop that runs the game
    player1.player_hand = []
    print("You have {} chips.".format(player1.chips))
    wager_check = True   
    Cards = deck.Deck(ranks, suits)             #creates card rank and suits, store card values as values of the keys ranks 
    Deck = Cards.deckShuffle(Cards.deckCreator())
    Dealer = dealer.Dealer([])
    #print(Deck)
    while wager_check:                         #(3l)makes sure that wager is in the correct format and within the bounds
        try:
            wager = int(input("Please enter your wager:\n"))
            if wager < 5:
                raise(errors.SmallerThan5("Your wager must be at least 5 chips!"))
            elif wager > player1.chips:
                raise(errors.ChipOverFlow("Your wager cannot be bigger than the number of chips you have!"))

            wager_check = False
            player1.chips -= wager
            print("Wager: {}\nRemanining chips: {}".format(wager, player1.chips))

        except errors.SmallerThan5 as s5:
            print(s5)

        except errors.ChipOverFlow as co:
            print(co)

        except ValueError:
            print("Your wager must be an integer!")
    #print(Deck)
    Dealer.dealCard(Deck, player1.player_hand, 2)
    Dealer.dealCard(Deck, Dealer.dealer_hand, 2)
    print("Your initial hand: {}, {}".format(player1.player_hand[0], player1.player_hand[1]))
    print("Dealer's initial hand: {}, {}".format(Dealer.dealer_hand[0], "Face down"))
    #print(Deck)
    if card_value_finder(player1.player_hand) == 21:
        print("Player wins")
    
        player1.chips += wager*3
        replay = True
        while replay:                                         
                options = input("Do you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":                            #(3c)checks whether the player wants to quit or replay
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")
    else:
        hit_check = True
        while hit_check:                                        #(4l)makes the player add cards to his deck
                                                                #runs as long as the sum of the cards is smaller than 21 and the player wants to hit
            print("\nYour current hand:", *player1.player_hand)
            print("Current card value:", card_value_finder(player1.player_hand))
            print("\nDealer's current hand:", *Dealer.dealer_hand)
            print("Dealer's current card value:", card_value_finder(Dealer.dealer_hand))

            hos = input('\nYou have two options hit or stand:\n')
            if hos == 'hit':
                player1.hit_Player(Deck)
                if card_value_finder(player1.player_hand) > 21:
                    hit_check = False
                                                                    #(4c)checks whether the player wants to hit or stand
            elif hos == 'stand':
                hit_check = False
                dealer_hit = True
                while dealer_hit:
                    if card_value_finder(Dealer.dealer_hand) <= 21: 
                        if card_value_finder(Dealer.dealer_hand) <= 17:
                            Dealer.hit_Dealer(Deck)
                        elif 17<card_value_finder(Dealer.dealer_hand)<=21:
                            dealer_hit = False
                    else:
                        dealer_hit = False
                
            else:
                print("Invalid input. The only two options are hit or stand.")

        print("\nDealer's final hand:", *Dealer.dealer_hand)
        print("Your final hand:", *player1.player_hand)                         #(5c)the ifs below determines who the winner is
        if card_value_finder(player1.player_hand) > 21:
            print("\nYou busted.")
            print("\nAll the wager is lost.")
            replay = True
            while replay:
                options = input("\nDo you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")
        
        elif card_value_finder(Dealer.dealer_hand) > 21:
            print("\nDealer busted. You won!")
            print("\nYou earned twice the wager.")
            player1.chips += 2*wager
            replay = True
            while replay:
                options = input("\nDo you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")
        

        elif card_value_finder(Dealer.dealer_hand) > card_value_finder(player1.player_hand):
            print("\nDealer won the game!")
            replay = True
            while replay:
                options = input("\nDo you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")
        elif card_value_finder(Dealer.dealer_hand) < card_value_finder(player1.player_hand):
            print("\nYou won the game!")
            player1.chips += 2*wager
            replay = True
            while replay:
                options = input("\nDo you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")
        elif card_value_finder(Dealer.dealer_hand) == card_value_finder(player1.player_hand):
            print("\nDraw")
            print("\nYou neither lost nor earned anything.")
            replay = True
            while replay:
                options = input("Do you want to replay? Y or N:\n")
                if options == "Y":
                    replay = False
                elif options == "N":
                    replay = False
                    game_loop_check = False

                else:
                    print("You should choose Y or N.")

print("Game Over!")         


        
            





