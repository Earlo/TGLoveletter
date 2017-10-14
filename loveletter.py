import random

class Message:
    to = None
    data = None
    def __init__(self, string, receivers):
        data = string
        to = receivers

class LoveLetter:
    deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
    last_discard = None
    random.shuffle(deck)
    turnNumber = 0
    player = None
    names = None
    burn = None

    def __init__(self, players):
        if(len(players) > 14):
            raise ValueError("Too many players")
            return
        player = [None] * len(players)
        for p in player:
            p = LoveLetterPlayer(self.deck.pop())
        self.draw(0)
        self.burn = self.deck.pop() #Burn
        self.names = players

    def play(self, card, target_player = 0, card_guess = 0):
        if card not in self.player[self.turnNumber].cards:
            raise ValueError("Player does not have card")
            return
        self.player[self.turnNumber].remove(card)

        public_message = ""
        private_messages = None

        if card == 8: #Princess
            player[self.turnNumber].alive = False
            public_message += "Player " + names[self.turnNumber] + " discarded their Princess and dieded! RIP\n"
    
        if card == 7: #Countess
            public_message += "Player " + names[self.turnNumber] + " discarded their Countess, but y tho?\n"

        if card == 6: #King
            if(player[self.turnNumber].has(7)):
                raise ValueError("Can't discard the King if player has the Countess")
            save = player[target_player].cards[0]
            player[target_player].cards[0] = names[turnNumber].cards[0]
            player[self.turnNumber].cards[0] = save
            public_message += "Player " + names[self.turnNumber] + " discarded their King and switched their hand with " + names[target_player] + "\n"
            private_messages = [Message("You have now a " + player[self.turnNumber].cards[0], self.turnNumber), Message("You have now a " + player[target_player].cards[0], target_player)]

        if card == 5: #Prince
            if(player[self.turnNumber].has(7)):
                raise ValueError("Can't discard a Prince if player has the Countess")
            else:
                public_message += "Player " + self.names[turnNumber] + " discarded their Prince targeting player" + self.names[target_player] + "\n"

        if card == 4: #Handmaiden
            player[turnNumber].handMaiden = True
            public_message += "Player " + self.names[turnNumber] + " discarded their Handmaiden.\n"

        if card == 3: #Baron
            if(player[turnNumber].cards[0] > player[another_player].cards[0]):
                player[turnNumber].alive = False
                public_message += "Player " + self.names[turnNumber] + " discarded their Baron and had a larger dick than " + self.names[target_player] + "\n"
            elif(player[turnNumber].cards[0] < player[another_player].cards[0]):
                player[another_player] = False
                public_message += "Player " + self.names[turnNumber] + " discarded their Baron and had a smaller dick than " + self.names[target_player] + "\n"

        if card == 2: #Priest
            player[turnNumber].remove(card)
            public_message += "Player " + self.names[turnNumber] + " discarded their Priest targeting player " + self.names[target_player] + "\n"
            private_messages = Message(self.names[target_player] + " has a " + player[target_player].cards[0], target_player) + "\n" 

        if card == 1: #Guard
            if(guess_card in player[another_player].cards):
                player[another_player].alive = False
                public_message += "Player " + self.names[turnNumber] + " discarded their Guard targeting player " + self.names[target_player] + " who died for having a " + card_guess + "\n"
            else:
                public_message += "Player " + self.names[turnNumber] + " discarded their Guard targeting player " + self.names[target_player] + " who did not have a " + card_guess + "\n"


        self.advance()
        return [public_message, private_messages]

    # Returns index of player who has the turn
    def turn(self):
        return self.turnNumber

    # Moves the turn forward
    def advance(self):
        turnNumber = (self.turnNumber + 1) % players
        while(player.alive == False):
            turnNumber = (self.turnNumber + 1) % players

    # Returns the amount of cards left
    def cardsLeft(self):
        return len(self.deck)

    # Draws a new card, returns the card drawn
    def draw(self, player_number):
        if(len(self.deck) == 0 or players_left() == 0):
            return 0
        new_card = self.deck.pop()
        self.player[player_number].cards[1] = new_card
        return new_card
    # Returns amount of players alive
    def players_left(self):
        n = 0
        for i in self.player:
            if i.alive:
                n += 1
        return n

    # Returns name of current playing player
    def current_name(self):
        return self.names[self.turnNumber]

class LoveLetterPlayer:
    handmaiden = False
    cards = [None] * 2
    alive = True
    def __init__(self, card):
        self.cards[0] = card

    def remove(self, card):
        handMaiden = False
        if(self.cards[1] == card):
            self.cards[1] = None
            return True
        elif(self.cards[0] == card):
            self.cards[0] = self.cards[1]
            self.cards[1] = None
            return True
        return False
