import random


def createDeck() -> dict:
    deck = dict()
    suite = ["Heart", "Spade", "Diamond", "Club"]
    face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    value = 1
    for type in suite:
        for name in face:
            deck.update({name + " of " + type: value})
            value += 1
        value = 1
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


