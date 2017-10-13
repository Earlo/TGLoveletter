#from telegram.ext import Updater, CommandHandler
import telegram
import pprint

from messages import *

bot = telegram.Bot(token='TOKENHERE')


while ( not done ):
	try:
		updates = bot.getUpdates( offset = 	-1 ,limit = 1 )
		while (updates):
			u = updates.pop()
			#
			#if not u.message.chat.id in chatStates:
			#	chatStates[u.message.chat.id] = {'s':State.INTRO,'id':u.message.message_id, 'current':random.randint(0,len(data))}
			#	bot.sendMessage(chat_id=u.message.chat.id, text= GREET )
			#make sure unique post
			#if (chatStates[u.message.chat.id]['id'] != u.message.message_id):
				#pp.pprint(dir(u.message))
			#	pp.pprint(u.message.text)

			if (u.message.text == "/help"):
				bot.sendMessage(chat_id=u.message.chat.id, text= HELP )

	except KeyboardInterrupt:
		print("\nexitting super gracefully-des\n")
		done = True
	except Exception as e:
		print(e)
		print("something went wrong ^^' ")

