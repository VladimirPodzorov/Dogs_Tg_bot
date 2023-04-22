import telebot
from telebot import util
from telebot import types
from Settings import TG_BOT_SETTINGS
from siteAPI.box_office import lst_box_office, lst

token = TG_BOT_SETTINGS()
bot = telebot.TeleBot(token.tg_api.get_secret_value())


@bot.message_handler(commands=['start'])
def hello(message):
	bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def help_info(message):
	with open('../commands.txt', 'r', encoding='utf-8') as text:
		for line in util.smart_split(text.read(), 3000):
			bot.send_message(message.chat.id, line)


@bot.message_handler(commands=['high'])
def low(message):
	kb = types.InlineKeyboardMarkup(row_width=2)
	btn_1 = types.InlineKeyboardButton('Сборы', callback_data='Сборы')
	btn_2 = types.InlineKeyboardButton('Рейтинг', callback_data='Рейтинг')
	kb.add(btn_1, btn_2)

	bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
	cashbox_rating = lst_box_office(lst)
	if call.message:
		if call.data == 'Сборы':
			bot.send_message(call.message.chat.id, 'Введите количество фильмов')

			@bot.message_handler(content_types=['text'])
			def content(message):
				try:
					count = int(message.text)
					for i, v in enumerate(cashbox_rating):
						img, name, cash = map(lambda x: x, v)
						bot.send_message(call.message.chat.id, f'<b>Название:</b> {name}\n'
						f'<b>Сборы за неделю:</b> {cash}\n{img}', parse_mode='HTML')
						count -= 1
						if count == 0:
							break
				except ValueError:
					bot.send_message(call.message.chat.id, 'Вводимый текст должен быть цифрой')


if __name__ == '__main__':
	bot.polling()
