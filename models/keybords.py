from telebot import types

keyboard_authorization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_authorization.add(types.KeyboardButton('Да, я хочу сохранить'))
keyboard_authorization.add(types.KeyboardButton('Нет, я хочу изменить'))


keyboard_specialization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_specialization.add(types.KeyboardButton('specialization_1'))
keyboard_specialization.add(types.KeyboardButton('specialization_2'))
keyboard_specialization.add(types.KeyboardButton('specialization_3'))


triple_answer = types.ReplyKeyboardMarkup(row_width=2)
keyboard_specialization.add(types.KeyboardButton('Хорошие'))
keyboard_specialization.add(types.KeyboardButton('Удовлетворительные'))
keyboard_specialization.add(types.KeyboardButton('Неудовлетворительные'))


quad_answer = types.ReplyKeyboardMarkup(row_width=2)
keyboard_specialization.add(types.KeyboardButton('Полностью обеспечены'))
keyboard_specialization.add(types.KeyboardButton('Частично обеспечены'))
keyboard_specialization.add(types.KeyboardButton('Слабо обеспечены'))
keyboard_specialization.add(types.KeyboardButton('Не обеспечены'))

