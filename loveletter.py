import random

class LoveLetter:
    deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
    random.shuffle(cards)
    turnNumber = 0

    def __init__(players):
        if(players > 15):
            raise ValueError("Too many players")
            return

        player = [None] * players
        for p in player:
            p = new LoveLetterPlayer(deck.pop())
        p[0].second = deck.pop()

    def turn():
        return turnNumber

    def play(card):
        if card not in player[turnNumber]:
            raise ValueError("Player does not have card")
            return
        if card == 8:
            return turnNumber #This player gets killed
    
    def play(card, another_player):
        if card not in player[turnNumber]:
            raise ValueError("Player does not have card")
            return
        if card == 8:
            return turnNumber #This player gets killed

class LoveLetterPlayer:
    handmaiden = 0
    first = 0
    second = 0
    def __init__(card):
        first = card
