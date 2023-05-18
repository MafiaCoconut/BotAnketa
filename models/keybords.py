from telebot import types

keyboard_authorization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_authorization.add(types.KeyboardButton('Да, я хочу сохранить'))
keyboard_authorization.add(types.KeyboardButton('Нет, я хочу изменить'))


keyboard_specialization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_specialization.add(types.KeyboardButton('specialization_1'))
keyboard_specialization.add(types.KeyboardButton('specialization_2'))
keyboard_specialization.add(types.KeyboardButton('specialization_3'))


# keyboard_to_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard_to_menu.add(types.KeyboardButton('Menu'))
