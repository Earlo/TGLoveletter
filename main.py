#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
#import loveletter

pp = pprint.PrettyPrinter(indent=4)

from messages import *

chats = {}
games = {}

#bot = telegram.Bot(token='468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')

updater = Updater('468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')


def start(bot, update):
	update.message.reply_text('Hello World!')

def help(bot, update):
	update.message.reply_text(HELP)

def enter(bot, update):
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id

	update.message.reply_text( "{} from {} in {}".format(messageID, playerID, chatID) )
	if not chatID in chats.keys():
		update.message.reply_text( "Starting gameroom from {}".format( chatID ) )
		chats[chatID] = "JEBUBU"
	else:
		update.message.reply_text( "already game in {}.".format( chatID ) )
		AddPlayer():

def AddPlayer(ChatID):

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
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()
