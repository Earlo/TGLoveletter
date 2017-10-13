#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
#import loveletter

pp = pprint.PrettyPrinter(indent=4)

from messages import *

chats = {}
games = {}

updater = Updater('468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')


def start(bot, update):
	update.message.reply_text('Hello World!')

def help(bot, update):
	update.message.reply_text(HELP)
	
def rules(bot, update):
	update.message.reply_text(RULES)
	
def lore(bot, update):
	update.message.reply_text(LORE)

def enter(bot, update):
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id

	update.message.reply_text( "{} from {} in {}".format(messageID, playerID, chatID) )
	if not chatID in chats.keys():
		update.message.reply_text( "Starting gameroom from {}".format( chatID ) )
		chats[chatID] = { 'players': set() }
	else:
		update.message.reply_text( "already game in {}.".format( chatID ) )
	AddPlayer(update, chatID, playerID)

def AddPlayer(update, ChatID, PlayerID):
	print(chats, ChatID)
	print(chats[ChatID]['players'])
	try:
		chats[ChatID]['players'].add(PlayerID)
		print(chats[ChatID]['players'])
		update.message.reply_text( "Added {}".format( PlayerID ) )
	except:
		print("?")
		update.message.reply_text( "wat" )

def ListPlayers(bot, update):
	chatID = update.message.chat.id
	update.message.reply_text( repr( chats[chatID]['players'] ) )

def startGame(bot, update):
	if len(list(games.keys())) > 0:
		nkey = max(list(games.keys())) + 1 
	else:
		nkey = 0
	if len(update.message.text.split(" ")) >= 2:
		pcount = int ( update.message.text.split(" ")[1] )
		update.message.reply_text("Created game #{} with {} players".format(nkey, pcount))
		games[nkey] = "JEBU"#loveletter.LoveLetter()

		print(nkey, pcount)
	else:
		update.message.reply_text("please specify player count")


	
	#update.message.reply_text(update.message.text)
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('enter', enter))
updater.dispatcher.add_handler(CommandHandler('list', ListPlayers))

updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('rules', rules))
updater.dispatcher.add_handler(CommandHandler('lore', lore))

updater.start_polling()
updater.idle()
