import random
import mappings

class Message:
	to = None
	data = None
	def __init__(self, string, receivers):
		data = string
		to = receivers

class LoveLetter:
	deck = [1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
	random.shuffle(deck)

	def __init__(self, playerNames):
		self.turnNumber = 0
		self.last_discard = None

		if(len(playerNames) > 14):
			raise ValueError("Too many players")
			return
		self.players = []
		for i  in range(len(playerNames)):
			self.players.append(LoveLetterPlayer(self.deck.pop(), playerNames[i]))
		self.draw(0)
		self.burn = self.deck.pop() #Burn
		self.names = playerNames

	def play(self, card, target_player = 0, card_guess = 0):
		print(mappings.CARDS)
		card = mappings.CARDS[card]
		print("mapped into",card)

		if card not in self.current_cards():
			raise ValueError("Tried to play {}, when the hand consists of {}".format(card, repr(self.current_cards())) )
		self.players[self.turnNumber].remove(card)

		if self.players[target_player].handMaid
			raise ValueError("Invalid target, target has a Handmaid played!")

		if not self.players[target_player].alive:
			raise ValueError("Invalid target, target is out of the game!")

		if 1 == card_guess:
			raise ValueError("Invalid guess, cannot guess Guard.")

		public_message = ""
		private_messages = None
		print("kek")
		if card == 8: #Princess
			self.players[self.turnNumber].alive = False
			public_message += "Player " + self.current_name() + " discarded the Princess, dropping out of the game!\n"

		elif card == 7: #Countess
			public_message += "Player " + self.current_name() + " discarded the Countess...but for what reason?\n"

		elif card == 6: #King
			if( 7 in self.players[self.turnNumber].cards):
				raise ValueError("Can't discard the King if you have the Countess")
			save = self.players[target_player].cards[0]
			self.players[target_player].cards[0] = self.players[self.turnNumber].cards[0]
			self.players[self.turnNumber].cards[0] = save
			public_message += "Player " + self.current_name() + " discarded the King and switched their hand with " + self.names[target_player] + "\n"
			private_messages = [Message("You have now a " + self.players[self.turnNumber].cards[0], self.turnNumber), Message("You have now a " + self.players[target_player].cards[0], target_player)]

		elif card == 5: #Prince
			if (7 in self.players[self.turnNumber].cards):
				raise ValueError("Can't discard a Prince if you have the Countess")
			elif (8 in self.players[target_player].cards):
				self.players[target_player].alive = False
				public_message += "Player " + self.current_name() + " discarded their prince targeting player " + self.names[target_player] + "Who died discarding the Princess!\n"
			else:
				public_message += "Player " + self.current_name() + " discarded their prince targeting player " + self.names[target_player] + "\n"

		elif card == 4: #Handmaiden
			self.players[self.turnNumber].handMaid = True
			public_message += "Player " + self.current_name() + " discarded their Handmaid. They cannot be targeted before their next turn. \n"

		elif card == 3: #Baron
			if(self.players[self.turnNumber].cards[0] > self.players[target_player].cards[0]):
				self.players[target_player].alive = False
				public_message += "Player " + self.current_name() + " discarded their Baron and had a larger or equal dick than " + self.names[target_player] + "\n"
			elif(self.players[self.turnNumber].cards[0] < self.players[target_player].cards[0]):
				self.players[self.turnNumber] = False
				public_message += "Player " + self.current_name() + " discarded their Baron and had a smaller dick than " + self.names[target_player] + "\n"
			else:
				public_message += "Player " + self.current_name() + " discarded their Baron and had a dick of the same size as " + self.names[target_player] + "\n"


		elif card == 2: #Priest
			self.players[self.turnNumber].remove(card)
			public_message += "Player " + self.current_name() + " discarded their Priest targeting player " + self.names[target_player] + "\n"
			private_messages = Message(self.names[target_player] + " has a " + str(self.players[target_player].cards[0]), target_player)

		elif card == 1: #Guard
			if(card_guess in self.players[target_player].cards):
				self.players[target_player].alive = False
				public_message += "Player " + self.current_name() + " discarded their guard targeting player " + self.names[target_player] + " who died for having a " + str(card_guess) + "\n"
			else:
				public_message += "Player " + self.current_name() + " discarded their guard targeting player " + self.names[target_player] + " who did not have a " + str(card_guess) + "\n"


		newCard = self.advance()
		return [public_message, private_messages]

	# Returns index of player who has the turn
	def turn(self):
		return self.turnNumber

	# Moves the turn forward
	def advance(self):
		turnNumber = (self.turnNumber + 1) % len(self.players)
		while(self.players[turnNumber].alive == False):
			turnNumber = (self.turnNumber + 1) % len(self.players)
		draw(self.turnNumber)

	# Returns the amount of cards left
	def cardsLeft(self):
		return len(self.deck)

	# Draws a new card, returns the card drawn
	def draw(self, player_number):
		if(len(self.deck) == 0 or self.players_left() == 0):
			return 0
		new_card = self.deck.pop()
		self.players[player_number].cards.append( new_card )
		return new_card
	# Returns amount of players alive
	def players_left(self):
		n = 0
		for i in self.players:
			if i.alive:
				n += 1
		return n

	# Returns name of current playing player
	def current_name(self):
		return self.players[self.turnNumber].name

	def current_cards(self):
		return self.players[self.turnNumber].cards

class LoveLetterPlayer:
	def __init__(self, card, name):
		self.handMaid = False
		self.alive = True
		self.cards = [card]
		self.name = name

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
