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
            raise ValueError("There is already the max amount of players in the game.")
            return
        player = [None] * len(players)
        for p in player:
            p = LoveLetterPlayer(deck.pop())
        p[0].second = deck.pop()
        burn = deck.pop() #Burn
        names = players

    def play(self, card, target_player = 0, card_guess = 0):
        if card not in player[turnNumber].cards:
            raise ValueError("You don't have that card in your hand...")
            return
        player[turnNumber].remove(card)

        public_message = ""
        private_messages = None

        if card == 8: #Princess
            player[turnNumber].alive = False
            public_message += "Player " + names[turnNumber] + " discarded the Princess and dieded! RIP\n"
    
        if card == 7: #Countess
            public_message += "Player " + names[turnNumber] + " discarded the Countess, but y tho?\n"

        if card == 6: #King
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard the King if player has the Countess")
            save = player[target_player].cards[0]
            player[target_player].cards[0] = names[turnNumber].cards[0]
            player[turnNumber].cards[0] = save
            public_message += "Player " + names[turnNumber] + " discarded their King and switched his hand with " + names[target_player] + "\n"
            private_messages = [Message("You now have a " + player[turn_number].cards[0], turn_number), Message("You now have a " + player[target_player].cards[0], target_player)]

        if card == 5: #Prince
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard a Prince if player has the Countess")
            public_message += "Player " + names[turnNumber] + " discarded their Prince.\n"

        if card == 4: #Handmaiden
            player[turnNumber].handMaiden = True
            public_message += "Player " + names[turnNumber] + " discarded their whore Handmaiden.\n"

        if card == 3: #Baron
            if(player[turnNumber].cards[0] > player[another_player].cards[0]):
                player[turnNumber].alive = False
                public_message += "Player " + names[turnNumber] + " discarded their Baron and had a larger dick than " + names[target_player]
            elif(player[turnNumber].cards[0] < player[another_player].cards[0]):
                player[another_player] = False
                public_message += "Player " + names[turnNumber] + " discarded their Baron and had a smaller dick than " + names[target_player]

        if card == 2: #Priest
            player[turnNumber].remove(card)
            public_message += "Player " + names[turnNumber] + " discarded his Priest, targeting player " + names[target_player]
            private_messages = Message(names[target_player] + " has a " + player[target_player].cards[0], target_player)

        if card == 1: #Guard
            if(guess_card in player[another_player].cards):
                player[another_player].alive = False
                public_message += "Player " + names[turnNumber] + " discarded their guard targeting player " + names[target_player] + " who died for having a " + card_guess
            else:
                public_message += "Player " + names[turnNumber] + " discarded their guard targeting player " + names[target_player] + " who did not have a " + card_guess


        this.advance()
        return [public_message, private_messages]

    # Returns index of player who has the turn
    def turn(self):
        return turnNumber

    # Moves the turn forward
    def advance(self):
        turnNumber = (turnNumber + 1) % players
        while(player.alive == False):
            turnNumber = (turnNumber + 1) % players

    # Returns the amount of cards left
    def cardsLeft(self):
        return len(deck)

    # Draws a new card, returns the card drawn
    def draw(self, player_number):
        if(len(deck) == 0 or players_left() == 0):
            return 0
        new_card = deck.pop()
        player[player_number].cards[1] = new_card
        return new_card
    # Returns amount of players alive
    def players_left(self):
        n = 0
        for i in player:
            if i.alive:
                n += 1
        return n

    # Returns name of current playing player
    def current_name(self):
        return names[turnNumber]

class LoveLetterPlayer:
    handmaiden = False
    cards = [None] * 2
    alive = True
    def __init__(self, card):
        cards[0] = card

    def remove(self, card):
        handMaiden = False
        if(cards[1] == card):
            cards[1] == None
            return True
        elif(cards[0] == card):
            cards[0] == cards[1]
            cards[1] == None
            return True
        return False
