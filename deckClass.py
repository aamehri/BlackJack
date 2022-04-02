# Code designed and written by Andrew Mehri, 2022
# Please contact drewprof@yahoo.com for permission to use this code.

import random

class deck:
    def __init__(self):
        self.suite = ["Heart", "Spade", "Diamond", "Club"]
        self.face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


    # generic values for cards in deck
    def createDeckRegular(self) -> dict:
        deck = dict()
        value = 1
        for type in self.suite:
            for name in self.face:
                deck.update({name + " of " + type: value})
                value += 1
            value = 1
        return deck


    # values for cards in a Blackjack deck
    def createDeckBlackJack(self) -> dict:
        deck = dict()
        value = 1
        for type in self.suite:
            for name in self.face[0:10]:
                deck.update({name + " of " + type: value})
                value += 1
            value = 10
            for name in self.face[10:13]:
                deck.update({name + " of " + type: value})
            value = 1
        return deck


    # values for card in a Poker deck
    def createDeckPoker(self) -> dict:
        deck = dict()
        # to be designed
        return deck


    def shuffleDeck(deck) -> list:
        cards = list()
        for card in deck.keys():
            cards.append(card)
        random.shuffle(cards)
        return cards


    def serveCard(cards) -> str:
        return cards.pop()


    def getCardValue(card, deck) -> int:
        return deck[card]


    def getHandValue(hand, deck) -> int:
        count = 0
        for card in hand:
            count += deck.getCardValue(card, deck)
        return count


