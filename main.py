#from telegram.ext import Updater, CommandHandler
import telegram
import pprint
pp = pprint.PrettyPrinter(indent=4)

from messages import *

chatStates = {}

bot = telegram.Bot(token='468086505:AAGr_hubo_N0hjIR7ouUkZZvoHnhFl4ngr4')

done = False

while ( not done ):
	try:
		updates = bot.getUpdates( offset = 	-1 ,limit = 1 )
		while (updates):
			u = updates.pop()

			#make sure unique post
			if not u.message.chat.id in chatStates:
				chatStates[u.message.chat.id] = {'LastMessageId':u.message.message_id, 'game':[]}
				bot.sendMessage(chat_id=u.message.chat.id, text= GREET )
			if (chatStates[u.message.chat.id]['LastMessageId'] != u.message.message_id):
				#pp.pprint(dir(u.message))
				pp.pprint(u.message.text)
				if (u.message.text == "/help"):
					bot.sendMessage(chat_id=u.message.chat.id, text= HELP )
				elif (u.message.text == "/rules"):
					bot.sendMessage(chat_id=u.message.chat.id, text= RULES)
				elif (u.message.text == "/lore"):
					bot.sendMessage(chat_id=u.message.chat.id, text= LORE)

				chatStates[u.message.chat.id]['LastMessageId'] = u.message.message_id

	except KeyboardInterrupt:
		print("\nexitting super gracefully-des\n")
		done = True
	except Exception as e:
		print(e)
		print("something went wrong ^^' ")

