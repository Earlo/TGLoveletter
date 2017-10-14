#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
#import loveletter

pp = pprint.PrettyPrinter(indent=4)

from messages import *

chats = {}

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
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id

	#update.message.reply_text( "{} from {} in {}".format(messageID, playerID, chatID) )
	if not chatID in chats:
		chats[chatID] = { 'players': set(), 'game': None }
		update.message.reply_text( "Starting game room from {}".format( chatID ) )
	else:
		update.message.reply_text( "Already a game in {}.".format( chatID ) )
	addPlayer(update, chatID, playerID)

def addPlayer(update, chatID, playerID):
	try:
		chats[chatID]['players'].add(playerID)
		update.message.reply_text( "Added {}".format( playerID ) )
	except:
		update.message.reply_text( "There was an error adding a player." )

def listPlayers(bot, update):
	chatID = update.message.chat.id
	update.message.reply_text( repr( chats[chatID]['players'] ) )

def startGame(bot, update):
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id
	try:
		print("log: staring game with:" + repr( chats[chatID]['players'] ) )
		update.message.reply_text( repr( chats[chatID]['players'] ) )
		bot.sendMessage(parse_mode='Markdown', chat_id=playerID, text="I'll be sending your hand information privately from here!")

	except:
		update.message.reply_text("No game going on in here, use /enter")


	
	#update.message.reply_text(update.message.text)
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('enter', enter))
updater.dispatcher.add_handler(CommandHandler('list', listPlayers))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('rules', rules))
updater.dispatcher.add_handler(CommandHandler('lore', lore))

updater.start_polling()
updater.idle()
