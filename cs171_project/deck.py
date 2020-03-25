#class for the deck
#Creates the attributes ranks, suits and functions deckCreator() deckShuffler()

from random import shuffle
class Deck:
 

    def __init__(self, ranks, suits):
        self.ranks = ranks.keys()
        self.suits = suits                                                      #instance init

    def deckCreator(self):                      #(4f)creates the deck out of the ranks and the suits
        deck = []
        for i in self.suits:                        #(5l)creates the deck by combining the suits and ranks
            for j in self.ranks:                               
                deck.append("{} {}".format(i, j))
        return deck

    def deckShuffle(self, deck):       #(5f)the function that shuffles the deck
        shuffle(deck)
        return deck



                                                                   