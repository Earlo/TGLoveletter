#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
from loveletter import LoveLetter

pp = pprint.PrettyPrinter(indent=4)

from messages import *

chats = {}
usersToIDs = {}

updater = Updater('468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')

def start(bot, update):
	chatID = update.message.chat.id
	update.message.reply_text('Hello World!')

def help(bot, update):
	chatID = update.message.chat.id
	bot.sendMessage(parse_mode='Markdown', chat_id=chatID, text=HELP)

def rules(bot, update):
	chatID = update.message.chat.id
	bot.sendMessage(parse_mode='Markdown', chat_id=chatID, text=RULES1)
	bot.sendMessage(parse_mode='Markdown', chat_id=chatID, text=RULES2)

def lore(bot, update):
	chatID = update.message.chat.id
	bot.sendMessage(parse_mode='Markdown', chat_id=chatID, text=LORE)

def enter(bot, update):
	print("a")
	chatID = update.message.chat.id
	print("b")
	playerUsername = update.message.from_user.username
	print("1")
	playerID = update.message.from_user.id
	print("3")
	messageID = update.message.message_id
	print("5")
	usersToIDs[playerUsername] = playerID
	print("6")

	if not chatID in chats:
		chats[chatID] = { 'players': set(), 'game': None }
		update.message.reply_text( "Starting game room from {}".format( chatID ) )
	else:
		update.message.reply_text( "Already a game in {}.".format( chatID ) )
	addPlayer(update, chatID, playerUsername)

def addPlayer(update, chatID, playerID):
	try:
		chats[chatID]['players'].add(playerID)
		update.message.reply_text( "Added {}".format( playerID ) )
	except Exception as e:
		update.message.reply_text( "There was an error in adding a player." )

def listPlayers(bot, update):
	chatID = update.message.chat.id
	update.message.reply_text( repr( chats[chatID]['players'] ) )

def startGame(bot, update):
	chatID = update.message.chat.id
	playerUsername = update.message.from_user.username
	playerID = update.message.from_user.id
	messageID = update.message.message_id
	usersToIDs[playerUsername] = playerID

	try:
		print("log: staring game with:" + repr( chats[chatID]['players'] ) )
		names = list( chats[chatID]['players'] )
		update.message.reply_text( repr( names ) )
		chats[chatID]['game'] = LoveLetter( list(chats[chatID]['players']) )
		bot.sendMessage(parse_mode='Markdown', chat_id=playerID, text="I'll be sending your hand information privately from here!")
		print("log: staring game with:" + repr( chats[chatID]['game'] ) )

	except Exception as e:
		print(e)
		bot.sendMessage(parse_mode='Markdown', chat_id=playerID, text="Error starting the game")

def play(bot, update):
	chatID = update.message.chat.id
	playerUsername = update.message.from_user.username
	playerID = update.message.from_user.id
	messageID = update.message.message_id
	usersToIDs[playerUsername] = playerID

	try:
		print(chats[chatID]['game'].current_name(), playerUsername)
		if chats[chatID]['game'].current_name() == playerUsername:

			bot.sendMessage(parse_mode='Markdown', chat_id=playerID, text="Your cards are  \n/"+'\n/'.join(map(str, chats[chatID]['game'].current_cards())))
		else:
			update.message.reply_text( "Not your turn...")
	except Exception as e:
		update.message.reply_text( "No game: " + e )



#update.message.reply_text(update.message.text)
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('enter', enter))
updater.dispatcher.add_handler(CommandHandler('play', play))

updater.dispatcher.add_handler(CommandHandler('list', listPlayers))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('rules', rules))
updater.dispatcher.add_handler(CommandHandler('lore', lore))

updater.start_polling()
updater.idle()
