# Code designed and written by Andrew Mehri, 2022
# Please contact drewprof@yahoo.com for permission to use this code.

import random
# global data
suite = ["Heart", "Spade", "Diamond", "Club"]
face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]


# generic values for cards in deck
def createDeckRegular() -> dict:
    deck = dict()
    value = 1
    for type in suite:
        for name in face:
            deck.update({name + " of " + type: value})
            value += 1
        value = 1
    return deck


# values for cards in a Blackjack deck
def createDeckBlackJack() -> dict:
    deck = dict()
    value = 1
    for type in suite:
        for name in face[0:10]:
            deck.update({name + " of " + type: value})
            value += 1
        value = 10
        for name in face[10:13]:
            deck.update({name + " of " + type: value})
        value = 1
    return deck


# values for card in a Poker deck
def createDeckPoker() -> dict:
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
        count += getCardValue(card, deck)
    return count


