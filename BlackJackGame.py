import deck


def main():
    # test
    myDeckVal = deck.createDeckBlackJack()
    print(myDeckVal)
    cardDeck = deck.shuffleDeck(myDeckVal)
    print(cardDeck)
    

main()
