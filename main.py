#from telegram.ext import Updater, CommandHandler
from telegram.ext import Updater, CommandHandler
import pprint
from loveletter import LoveLetter

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

	if not chatID in chats:
		chats[chatID] = { 'players': set(), 'game': None }
		update.message.reply_text( "Starting gameroom from {}".format( chatID ) )
	else:
		update.message.reply_text( "already game in {}.".format( chatID ) )
	AddPlayer(update, chatID, playerID)

def AddPlayer(update, chatID, playerID):
	try:
		chats[chatID]['players'].add(playerID)
		update.message.reply_text( "Added {}".format( playerID ) )
	except Exception as e:
		update.message.reply_text( "wat" )

def ListPlayers(bot, update):
	chatID = update.message.chat.id
	update.message.reply_text( repr( chats[chatID]['players'] ) )

def startGame(bot, update):
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id
	try:
		print("log: staring game with:" + repr( chats[chatID]['players'] ) )
		update.message.reply_text( repr( chats[chatID]['players'] ) )
		chats[chatID]['game'] = LoveLetter( list(chats[chatID]['players']) )
		bot.sendMessage(parse_mode='Markdown', chat_id=playerID, text="Moi Jäbä privailen tässä saatana")
		print("log: staring game with:" + repr( chats[chatID]['game'] ) )
	
	except Exception as e:
		print(e)
		update.message.reply_text("No game going on in here, use /enter")

def play(bot, update):
	chatID = update.message.chat.id
	playerID = update.message.from_user.id
	messageID = update.message.from_user.id
	try:
		print(chats[chatID]['game'])
		print(chats[chatID]['game'].current_name()) 
		if chats[chatID]['game'].current_name() == playerID:
			update.message.reply_text( "Sun vuoro" )
		else:
			update.message.reply_text( "Ei sun vuoro äbäj")
	except Exception as e:
		update.message.reply_text( "No game" )


	
#update.message.reply_text(update.message.text)
updater.dispatcher.add_handler(CommandHandler('newGame', startGame))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('enter', enter))
updater.dispatcher.add_handler(CommandHandler('play', play))

updater.dispatcher.add_handler(CommandHandler('list', ListPlayers))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('rules', rules))
updater.dispatcher.add_handler(CommandHandler('lore', lore))

updater.start_polling()
updater.idle()
