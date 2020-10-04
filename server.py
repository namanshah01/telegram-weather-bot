from bot import telegram_chatbot

bot = telegram_chatbot('telegram_config.cfg')

def make_reply(message):
	reply = None
	if message is not None:
		reply = 'boom boom'
	return reply

update_id = None
while True:
	print('...')
	updates = bot.get_updates(offset=update_id)
	updates = updates['result']
	if updates:
		for item in updates:
			update_id = item['update_id']
			try:
				message = str(item['message']['text'])
			except:
				message = None
			from_ = item['message']['chat']['id']
			reply = make_reply(message)
			bot.send_message(reply, from_)