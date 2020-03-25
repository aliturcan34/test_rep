#class for player
#this class includes simple player attributes such as player's hand and functions for betting money, hitting and standing
 
class Player:
    def __init__(self, chips, hand):
        self.chips = chips
        self.player_hand = hand
        

    def hit_Player(self, deck):
        self.player_hand.append(deck.pop())



        
        
