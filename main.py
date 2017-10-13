#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
pp = pprint.PrettyPrinter(indent=4)

from messages import *

chatStates = {}

#bot = telegram.Bot(token='468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')

updater = Updater('468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')


def start(bot, update):
	update.message.reply_text('Hello World!')

def help(bot, update):
	update.message.reply_text(HELP)

def startGame(bot, update):
	pp.pprint(dir(update))
	update.message.reply_text(HELP)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))

updater.start_polling()
updater.idle()
