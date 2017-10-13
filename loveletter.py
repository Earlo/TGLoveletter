import random

class Message:
    to = None
    data = None
    def __init__(string, receivers):
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

    def play(card, target_player = 0, card_guess = 0):
        if card not in player[turnNumber].cards:
            raise ValueError("Player does not have card")
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
            public_message += "Player " + names[turnNumber] + " discarded the king and switched his hand with " + names[target_player] + "\n"
            private_messages = [Message("You have now a " + player[turn_number].cards[0], turn_number), Message("You have now a " + player[target_player].cards[0], target_player)]

        if card == 5: #Prince
            if(player[turnNumber].has(7)):
                raise ValueError("Can't discard a Prince if player has the Countess")
            public_message += "Player " + names[turnNumber] + " discarded his prince.\n"

        if card == 4: #Handmaiden
            player[turnNumber].handMaiden = True
            public_message += "Player " + names[turnNumber] + " discarded his whore Handmaiden.\n"

        if card == 3: #Baron
            if(player[turnNumber].cards[0] > player[another_player].cards[0]):
                player[turnNumber].alive = False
                public_message += "Player " + names[turnNumber] + " discarded his Baron and had a larger dick than " + names[target_player]
            else if(player[turnNumber].cards[0] < player[another_player].cards[0]):
                player[another_player] = False
                public_message += "Player " + names[turnNumber] + " discarded his Baron and had a smaller dick than " + names[target_player]

        if card == 2: #Priest
            player[turnNumber].remove(card)
            public_message += "Player " + names[turnNumber] + " discarded his Priest targeting player " + names[target_player]
            private_messages = Message(names[target_player] + " has a " + player[target_player].cards[0], target_player)

        if card == 1: #Guard
            if(guess_card in player[another_player].cards):
                player[another_player].alive = False
                public_message += "Player " + names[turnNumber] + " discarded his guard targeting player " + names[target_player] + " who died for having a " + card_guess
            public_message += "Player " + names[turnNumber] + " discarded his guard targeting player " + names[target_player] + " who did not have a " + card_guess


        this.advance()
        return [public_message, private_messages]

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

    # Draws a new card, returns the card drawn
    def draw(player_number):
        if(len(deck) == 0 or players_left() == 0):
            return 0
        new_card = deck.pop()
        player[player_number).cards[1] = new_card
        return new_card
    # Returns amount of players alive
    def players_left():
        n = 0
        for i : player:
            if i.alive:
                n++
        return n

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
