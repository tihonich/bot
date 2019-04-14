# -*- coding: utf-8 -*-
import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)
def start_bot(bot, update):
	#print(update)
	mytext = """Привет {}!
Я простой бот и понимаю только команду {}""".format(update.message.chat.first_name, '/start')
	update.message.reply_text(mytext)

def chat(bot, update):
	#update.message.reply_text('Привет!')
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)
#Функция, которая соединяется  с платформой Telegram, 'тело' нашего бота
def main():
	updtr = Updater(settings.TELEGRAM_API_KEY)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))
	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started')
	main()
