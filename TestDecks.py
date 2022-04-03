import deck
import deckClass

def main():
    print("Procedural test")
    # test procedural method
    myDeckVal = deck.createDeckBlackJack()
    print(myDeckVal)
    cardDeck = deck.shuffleDeck(myDeckVal)
    print(cardDeck)
    card = deck.serveCard(cardDeck)
    print(cardDeck)

    print("\n\nObject Oriented test")
    # test with class to create an object and method
    myDeckVal2 = deckClass.deck()
    print("name of object: ", myDeckVal2)
    print(myDeckVal2.deck)
    myDeckVal2.createDeckBlackJack()
    print(myDeckVal2.deck)
    myDeckVal2.shuffleDeck()
    print(myDeckVal2.cards)
    aCard = myDeckVal2.serveCard()
    print(aCard, " its value = ", myDeckVal2.getCardValue(aCard))
    print(myDeckVal2.cards)
    myHand = []
    myHand.append(aCard)
    aCard = myDeckVal2.serveCard()
    myHand.append(aCard)
    handVal = myDeckVal2.getHandValue(myHand)
    print("my Hand: ", myHand)
    print("my Hand value: ", handVal)




    del myDeckVal2


main()
