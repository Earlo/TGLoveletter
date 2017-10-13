import random

class LoveLetter:
    deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
    last_discard = None
    random.shuffle(deck)
    turnNumber = 0
    player = None
    players_left = None
    burn = None


    def __init__(players):
        if(players > 14):
            raise ValueError("Too many players")
            return
        players_left = players

        player = [None] * players
        for p in player:
            p = LoveLetterPlayer(deck.pop())
        p[0].second = deck.pop()
        burn = deck.pop() #Burn

    def play(card, another_player = 0, card_guess = 0):
        if card not in player[turnNumber].cards:
            raise ValueError("Player does not have card")
            return

        if card == 8: #Princess
            player[turnNumber].alive = False
            self.advance()
            last_discard = card
            return turnNumber #This player gets killed
    
        if card == 7: #Countess
            player[turnNumber].remove(card)
            self.advance()
            last_discard = card
            return 0

        if card == 6: #King
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard the King if player has the Countess")
            player[turnNumber].remove(card)
            self.advance()
            last_discard = card
            return 0

        if card == 5: #Prince
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard a Prince if player has the Countess")
            player[turnNumber].remove(7)
            self.advance()
            last_discard = card
            return 0

        if card == 4: #HandMaiden
            player[turnNumber].remove(card)
            player[turnNumber].handMaiden = True
            self.advance()
            return 0

        if card == 3: #Baron
            player[turnNumber].remove(card)
            if(player[turnNumber].cards[0] > player[another_player].cards[0]):
                player[turnNumber].alive = False
                before_advance = turnNumber
                self.advance()
                return before_advance
            elif(player[turnNumber].cards[0] < player[another_player].cards[0]):
                player[another_player] = False
                self.advance()
                return another_player
            else:
                self.advance()
                return 0

        if card == 2: #Priest
            player[turnNumber].remove(card)
            self.advance()
            return 0

        if card == 1: #Guard
            player[turnNumber].remove(card)
            if(guess_card in player[another_player].cards):
                player[another_player].alive = False
                self.advance()
                return another_player
            self.advance()
            return 0

    # Returns index of player who has the turn
    def turn():
        return turnNumber

    # Moves the turn forward
    def advance():
        turnNumber = (turnNumber + 1) % players
        while(!player.alive):
            turnNumber = (turnNumber + 1) % players

    # Returns the amount of cards left
    def cardsLeft():
        return len(deck)

    #Draws a new card, returns the card drawn
    def draw(player_number):
        new_card = deck.pop()
        player[player_number).cards[1] = new_card
        return new_card

class LoveLetterPlayer:
    handmaiden = False
    cards = [None] * 2
    alive = True
    def __init__(card):
        cards[0] = card

    def remove(card):
        handMaiden = False
        if(cards[1] == card):
            cards[1] == None
            return True
        else if(cards[0] == card):
            cards[0] == cards[1]
            cards[1] == None
            return True
        return False
