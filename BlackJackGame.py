# Simple Blackjack game, by Andrew Mehri
# Please contact me for authorization to use this code drewprof@yahoo.com

import deckClass
def generateShuffeledCardDeck():
    myDeck = deckClass.deck()
    myDeck.createDeckBlackJack()
    myDeck.shuffleDeck()
    return myDeck.cards

def gameControl():
    try:
        choice = int(input("Enter 1 for another game, else 2 to end it: "))
    except ValueError:
        print("Please enter a number next time: Game terminated!")
    else:
        if choice == 1:
            return True
    return False


def twoCardsServe(shoe):
    firstHand = list()
    for count in range(2):
        firstHand.append(shoe.pop())
    return firstHand


def isBalckJack(hand):
    cardValues = deckClass.deck()
    cardValues.createDeckRegular()
    # print(cardValues.deck)
    # print(hand)
    if cardValues.getHandValue(hand) > 10 and (cardValues.deck.get(hand[0]) == 1 or cardValues.deck.get(hand[1]) == 1):

        del cardValues
        return True
    del cardValues
    return False


def main():
    MaxServes = 6
    dealerScore = 0
    playerScore = 0
    gameState = True
    while gameState:
        shoe = generateShuffeledCardDeck()
        print(shoe)
        for serve in range(MaxServes):
            print("Serve #", serve + 1)
            # initial serve 2 cards player, 2 cards dealer
            playerHand = twoCardsServe(shoe)
            # check if blackjack
            if isBalckJack(playerHand):
                print("Player got Black Jack")
                playerScore += 1

            else:
                dealerHand = twoCardsServe(shoe)
                if isBalckJack(dealerHand):
                    print("Dealer got Black Jack")
                    dealerScore += 1

            # if no blackjack, player with option to hit or stand
            # if no bust, or 21 by player, dealer served cards until higher than player hand or bust
            # update scores

        gameState = gameControl()
        del shoe
    print("Thank you for playing")
    print("Final Scores", "\nDealer: ", dealerScore, "\nPlayer: ", playerScore)


if __name__ == "__main__":
    main()