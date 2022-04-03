# Code designed and written by Andrew Mehri, 2022
# Please contact drewprof@yahoo.com for permission to use this code.

import random

class deck:
    def __init__(self):
        self.suite = ["Heart", "Spade", "Diamond", "Club"]
        self.face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.deck = dict()
        self.cards = list()
    # generic values for cards in deck
    def createDeckRegular(self):

        value = 1
        for type in self.suite:
            for name in self.face:
                self. deck.update({name + " of " + type: value})
                value += 1
            value = 1



    # values for cards in a Blackjack deck
    def createDeckBlackJack(self):

        value = 1
        for type in self.suite:
            for name in self.face[0:10]:
                self.deck.update({name + " of " + type: value})
                value += 1
            value = 10
            for name in self.face[10:13]:
                self.deck.update({name + " of " + type: value})
            value = 1



    # values for card in a Poker deck
    def createDeckPoker(self):
        pass
        # to be designed



    def shuffleDeck(self):

        for card in self.deck.keys():
            self.cards.append(card)
        random.shuffle(self.cards)



    def serveCard(self) -> str:
        return self.cards.pop()


    def getCardValue(self, card) -> int:
        return self.deck[card]


    def getHandValue(self, hand) -> int:
        count = 0
        for card in hand:
            count += self.getCardValue(card)
        return count


