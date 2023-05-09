from telebot import types

""" Клавиатура меню """
menu_kb = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
btn_1 = types.KeyboardButton('/help')
btn_2 = types.KeyboardButton('/low')
btn_3 = types.KeyboardButton('/high')
btn_4 = types.KeyboardButton('/custom')
btn_5 = types.KeyboardButton('/history')
menu_kb.add(btn_1, btn_2, btn_3, btn_4, btn_5)

""" Клавиатура категорий """
kb_choice = types.InlineKeyboardMarkup(row_width=2)
buttn_1 = types.InlineKeyboardButton('Линька', callback_data='shedding')
buttn_2 = types.InlineKeyboardButton('Дрессировка', callback_data='trainability')
buttn_3 = types.InlineKeyboardButton('Шум (лай)', callback_data='barking')
buttn_4 = types.InlineKeyboardButton('Охрана', callback_data='protectiveness')
kb_choice.add(buttn_1, buttn_2, buttn_3, buttn_4)

""" Клавиатура сортировки """
kb_sort = types.InlineKeyboardMarkup(row_width=2)
bt1 = types.InlineKeyboardButton('По весу', callback_data='weight')
bt2 = types.InlineKeyboardButton('По росту', callback_data='height')
kb_sort.add(bt1, bt2)

""" Клавиатура значений """
kb_grade = types.InlineKeyboardMarkup(row_width=2)
b1 = types.InlineKeyboardButton('1 из 5', callback_data='1')
b2 = types.InlineKeyboardButton('2 из 5', callback_data='2')
b3 = types.InlineKeyboardButton('3 из 5', callback_data='3')
b4 = types.InlineKeyboardButton('4 из 5', callback_data='4')
b5 = types.InlineKeyboardButton('5 из 5', callback_data='5')
kb_grade.add(b1, b2, b3, b4, b5)

""" Клавиатура для команды /custom """
kb_cust = types.InlineKeyboardMarkup(row_width=2)
bt1 = types.InlineKeyboardButton('По весу', callback_data='weight_cust')
bt2 = types.InlineKeyboardButton('По росту', callback_data='height_cust')
kb_cust.add(bt1, bt2)
