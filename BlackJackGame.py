import deck


def main():
    myDeckVal = deck.createDeckBlackJack()
    print(myDeckVal)
    cardDeck = deck.shuffleDeck(myDeckVal)
    print(cardDeck)
    

main()
