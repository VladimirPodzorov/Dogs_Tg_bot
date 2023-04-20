import telebot
from Settings import TG_BOT_SETTINGS


token = TG_BOT_SETTINGS()
bot = telebot.TeleBot(token.tg_api.get_secret_value())


@bot.message_handler(commands=['hello-world'])
def hello(message):
	bot.send_message(message.chat.id, 'Здравствуйте')


@bot.message_handler(content_types=['text'])
def answer(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.chat.id, 'Привет - привет!')


bot.polling()
