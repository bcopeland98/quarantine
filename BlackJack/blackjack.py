
import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val 
    
    def show(self):
        print(f"{self.value} of {self.suit}")
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
        

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()
    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()
    



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def getAces(self):
        aces = 0
        for card in self.hand:
            if card.getValue() == 1:
                aces += 1
        return aces

    def showHand(self):
        for card in self.hand:
            card.show()

    def getHand(self):
        return self.hand

    def getTop(self):
        top = self.hand[0]
        top.show()
    
    def scoreHand(self):
        score = 0
        aces = self.getAces()
        for card in self.hand:
            currVal = card.getValue()
            if currVal == 1:
                score += 11
            elif currVal >= 10:
                score += 10
            else:
                score += currVal

        while score > 21 and aces > 0:
            score -= 10
            aces -=1
            
        return score

        
        


class Game:
    def __init__(self):
        #self.name = name
        self.player = Player('Player')
        self.dealer = Player('Dealer')
        self.deck = Deck()
        self.deck.shuffle()
        self.dealerScore = 0
        self.playerScore = 0
    
    def scoreGame(self):
        self.dealerScore = self.dealer.scoreHand()
        self.playerScore = self.player.scoreHand()

        print("Your hand is: ")
        self.player.showHand()

        print("Dealer's hand is: ")
        self.dealer.showHand()

        print(f"Dealer score is {self.dealerScore}")
        print(f"Player score is {self.playerScore}")

        if self.playerScore > 21:
            print("You busted, you lose")
        elif self.dealerScore > 21:
            print("Dealer busted, you win!")
        elif self.playerScore > self.dealerScore:
            print("You beat the dealer, congrats!")
        else:
            print("you lost, sorry :(")
        
        

    def startGame(self):
        
        #give dealer and player 2 cards
        for i in range(0,2):
            self.dealer.draw(self.deck)
            self.player.draw(self.deck)
        
        #self.dealer.showHand()
        #show one of dealers cards
        print("Dealer's hand is", end = ' ')
        self.dealer.getTop()
        print("Your hand is: ")
        self.player.showHand()
        while self.player.scoreHand() <= 21:
            
            
            answer = input("Would you like to hit? Enter y or n ")

            if answer == 'y':
                self.player.draw(self.deck)
                print("Your hand is now: ")
                self.player.showHand()

            else:
                while self.dealer.scoreHand() < 17 and self.dealer.scoreHand() <= 21:
                    self.dealer.draw(self.deck)
                break
        self.scoreGame()
        
        

def main():
    while True:
        startGame = input("Hello! would you like to play Blackjack? (Enter y or n) ")
        if startGame =='y':
            newGame = Game()
            newGame.startGame()

        else:
            break



if __name__ == "__main__":
    main()


