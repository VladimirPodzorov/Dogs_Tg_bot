from Settings import TG_BOT_SETTINGS
import telebot
from telebot import util
from siteAPI.cust_req import get_cust_requests
from siteAPI.dog_finder import get_requests
from tgAPI.utils.keyboards import menu_kb, kb_choice, kb_sort, kb_grade, kb_cust
from tgAPI.utils.text_message import back_message
from database.model import *


db.connect()
db.create_tables([History])
token = TG_BOT_SETTINGS()
bot = telebot.TeleBot(token.tg_api.get_secret_value())

min_max = False
count_dogs = ''
grade = ''
choice_sort = ''
choice_value = ''
min_wght = ''
max_wght = ''
min_hght = ''
max_hght = ''


@bot.message_handler(commands=['history'])
def history(message):
	""" Команда /history - выводит из базы данных последние 10 запросов пользователя """
	count = 10
	for messag in History.select()[::-1]:
		bot.send_message(message.chat.id, messag.user_resp, parse_mode='HTML')
		count -= 1
		if count == 0:
			break


@bot.message_handler(commands=['start'])
def hello(message):
	""" Команда /start - приветствие. Запуск клавиатуры с доступными командами """
	bot.send_message(message.chat.id, 'Привет, я бот, который поможет подобрать собаку, в зависимости от характеристик.\n'
	                'Для поиска используйте команды меню.',
	                 reply_markup=menu_kb)


@bot.message_handler(commands=['help'])
def help_info(message):
	""" Команда /help - описание команд бота. """
	with open('commands.txt', 'r', encoding='utf-8') as text:
		for line in util.smart_split(text.read(), 3000):
			bot.send_message(message.chat.id, line)


@bot.message_handler(commands=['low'])
def low(message):
	""" Команда /low. """
	global min_max
	min_max = False
	bot.send_message(message.chat.id, 'В этом меню поиск идет по минимальным значениям: вес и рост.')
	bot.send_message(message.chat.id, 'Сделайте выбор\nсортировки поиска:', reply_markup=kb_sort)


@bot.message_handler(commands=['high'])
def high(message):
	""" Команда /high. """
	global min_max
	min_max = True
	bot.send_message(message.chat.id, 'В этом меню поиск идет по максимальным значениям: вес и рост.')
	bot.send_message(message.chat.id, 'Сделайте выбор\nсортировки поиска:', reply_markup=kb_sort)


@bot.message_handler(commands=['custom'])
def custom(message):
	""" Команда /custom. """
	bot.send_message(message.chat.id, 'Сделайте выбор\nсортировки поиска:', reply_markup=kb_cust)


@bot.message_handler(content_types=['text'])
def er_answer(message):
	""" Ответ на сообщения, которые могут вызвать ошибку """
	bot.send_message(message.chat.id, 'Я вас не понимаю.\nИспользуйте меню\nи доступные команды.')


def get_countdogs(message):
	""" Функция, которая принимает параментры. По которым пользователь хочет получить ответ.
	Передает их в метод запроса на сайт Api и выводит ответ в чат. """
	global min_max
	global count_dogs
	global choice_value
	global choice_sort
	global grade
	count_dogs = message.text
	try:
		if int(count_dogs) in range(21):
			data = get_requests(choice_value, grade, choice_sort, reverse=min_max)
			for item in data[:int(count_dogs)]:
				if isinstance(item, dict):
					bot.send_message(message.chat.id, back_message(item), parse_mode='HTML')
					History.create(user_id=message.chat.id, user_resp=back_message(item))

		else:
			bot.send_message(message.chat.id, 'Неверный ввод!\nВведите число от 1 до 20')
			bot.register_next_step_handler(message, get_countdogs)
	except ValueError:
		bot.send_message(message.chat.id, 'Вводимый текст должен быть цифрой')
		bot.register_next_step_handler(message, get_countdogs)


def get_custom_weight(message):
	global min_wght
	global max_wght
	try:
		min_wght, max_wght = map(lambda x: x, message.text.split(' '))
		if min_wght.isdigit() and max_wght.isdigit():
			bot.send_message(message.chat.id, 'Сколько показать собак?(не больше 20)')
			bot.register_next_step_handler(message, get_cust_dog)
		else:
			bot.send_message(message.chat.id, 'Вводимый текст должен быть цифрой.\n'
			'Введите минимальный и максимальный вес через пробел.')
			bot.register_next_step_handler(message, get_custom_weight)
	except ValueError:
		bot.send_message(message.chat.id, 'Что-то пошло не так!\nВведите минимальный и максимальный вес через пробел.')
		bot.register_next_step_handler(message, get_custom_weight)


def get_custom_height(message):
	global min_hght
	global max_hght
	try:
		min_hght, max_hght = map(lambda x: x, message.text.split(' '))
		if min_hght.isdigit() and max_hght.isdigit():
			bot.send_message(message.chat.id, 'Сколько показать собак?(не больше 20)')
			bot.register_next_step_handler(message, get_cust_dog)
		else:
			bot.send_message(message.chat.id, 'Вводимый текст должен быть цифрой.\n'
			'Введите минимальный и максимальный вес через пробел.')
			bot.register_next_step_handler(message, get_custom_height)
	except ValueError:
		bot.send_message(message.chat.id, 'Что-то пошло не так!\nВведите минимальный и максимальный вес через пробел.')
		bot.register_next_step_handler(message, get_custom_height)


def get_cust_dog(message):
	""" Вывод ответа для меню /custom """
	global count_dogs
	global min_wght
	global max_wght
	global min_hght
	global max_hght
	count_dogs = message.text
	try:
		if int(count_dogs) in range(21):
			data = get_cust_requests(min_weight=min_wght, max_weight=max_wght, min_height=min_hght, max_height=max_hght)
			if len(data) == 0:
				bot.send_message(message.chat.id, 'К сожалению, ничего не нашлось.')
			for msg in data[:int(count_dogs)]:
				bot.send_message(message.chat.id, back_message(msg), parse_mode='HTML')
				History.create(user_id=message.chat.id, user_resp=back_message(msg))
			min_wght = ''
			max_wght = ''
			min_hght = ''
			max_hght = ''
		else:
			bot.send_message(message.chat.id, 'Неверный ввод!\nВведите число от 1 до 20')
			bot.register_next_step_handler(message, get_cust_dog)
	except ValueError:
		bot.send_message(message.chat.id, 'Вводимый текст должен быть цифрой')
		bot.register_next_step_handler(message, get_cust_dog)


@bot.callback_query_handler(func=lambda call: True)
def action(call):
	""" Функция принимает и записывает ответы пользователя (инлайн клавиатуры). """
	global count_dogs
	global choice_value
	global choice_sort
	global grade
	if call.message:
		if call.data == 'weight' or call.data == 'height':
			choice_sort = call.data
			bot.send_message(call.message.chat.id, 'Выберите категорию поиска:', reply_markup=kb_choice)

		elif call.data == 'shedding' or call.data == 'trainability' or\
			call.data == 'barking' or call.data == 'protectiveness':
			choice_value = call.data
			bot.send_message(call.message.chat.id, f'Выберите значение {call.data} от 1 до 5', reply_markup=kb_grade)

		elif call.data == '1' or call.data == '2' or call.data == '3' or call.data == '4' or call.data == '5':
			grade = call.data
			bot.send_message(call.message.chat.id, 'Сколько показать собак?(не больше 20)')
			bot.register_next_step_handler(call.message, get_countdogs)

		elif call.data == 'weight_cust':
			bot.send_message(call.message.chat.id, 'Введите минимальный и максимальный вес через пробел.')
			bot.register_next_step_handler(call.message, get_custom_weight)

		elif call.data == 'height_cust':
			bot.send_message(call.message.chat.id, 'Введите минимальный и максимальный рост через пробел.')
			bot.register_next_step_handler(call.message, get_custom_height)
