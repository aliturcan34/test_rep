#class for dealer
#this class includes simple dealer attributes such as dealer's hand and functions for dealing cards and hitting.

class Dealer:
    def __init__(self, hand):
        self.dealer_hand = hand

    def dealCard(self, deck, hand, number):
        for _ in range(number):                                           #(2f)function that deals the card in the beginning of the game
            hand.append(deck.pop())

    
    def hit_Dealer(self,deck):                                        #(3f) function that enables the dealer to hit cards
        self.dealer_hand.append(deck.pop())
    




        
    



    

