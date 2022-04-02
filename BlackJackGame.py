import deck
import deckClass

def main():
    # test
    myDeckVal = deck.createDeckBlackJack()
    print(myDeckVal)
    cardDeck = deck.shuffleDeck(myDeckVal)
    print(cardDeck)

    # test with class to create an object and method
    myDeckVal2 = deckClass.deck()
    print(myDeckVal2.createDeckRegular())

    del myDeckVal2


main()
