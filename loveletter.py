import random

class LoveLetter:
    deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
    random.shuffle(deck)
    turnNumber = 0
    player = None

    def __init__(players):
        if(players > 15):
            raise ValueError("Too many players")
            return

        player = [None] * players
        for p in player:
            p = new LoveLetterPlayer(deck.pop())
        p[0].second = deck.pop()


    def play(card, another_player = 0):

        if card not in player[turnNumber]:
            raise ValueError("Player does not have card")
            return

        if card == 8:
            player[turnNumber].alive = False
            self.advance()
            return turnNumber #This player gets killed
    
        if card == 7:
            if(player[turnNumber].remove(7)):
                self.advance()
            return 0

        if card == 6:
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard the King if player has the Countess")

        if card == 5:
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard a Prince if player has the Countess")


    # Returns index of player who has the turn
    def turn():
        return turnNumber

    # Moves the turn forward
    def advance():
        turnNumber

    # Returns the amount of cards left
    def cardsLeft():
        return len(deck)


class LoveLetterPlayer:
    handmaiden = 0
    cards = [None] * 2
    alive = True
    def __init__(card):
        cards[0] = card

    def has(card):
        if(cards[2] == card):
            return 2
        else if(cards[0] == card):
            return 1
        else:
            return 0

    def remove(card):
        if(cards[1] == card):
            cards[1] == None
            return True
        else if(cards[0] == card):
            cards[0] == None
            return True
        return False
