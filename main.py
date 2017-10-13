#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
import loveletter

pp = pprint.PrettyPrinter(indent=4)

from messages import *

games = {}

#bot = telegram.Bot(token='468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')

updater = Updater('468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')


def start(bot, update):
	update.message.reply_text('Hello World!')

def help(bot, update):
	update.message.reply_text(HELP)

def startGame(bot, update):
	#pp.pprint(dir(update.message))
	if len(list(games.keys())) > 0:
		nkey = max(list(games.keys())) + 1 
	else:
		nkey = 0
	if len(update.message.text.split(" ")) >= 2:
		pcount = int ( update.message.text.split(" ")[1] )
		update.message.reply_text("Created game #{} with {} players".format(nkey, pcount))
		print(nkey, pcount)
	else:
		update.message.reply_text("please specify player count")


	#games[nkey] = loveletter.LoveLetter()
	
	#update.message.reply_text(update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))

updater.start_polling()
updater.idle()
