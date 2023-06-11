from telebot import types

keyboard_authorization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_authorization.add(types.KeyboardButton('Да, я хочу сохранить'))
keyboard_authorization.add(types.KeyboardButton('Нет, я хочу изменить'))


keyboard_yes_no = types.ReplyKeyboardMarkup(row_width=2)
keyboard_yes_no.add(types.KeyboardButton('Да'))
keyboard_yes_no.add(types.KeyboardButton('Нет'))


keyboard_specialization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_specialization.add(types.KeyboardButton('specialization_1'))
keyboard_specialization.add(types.KeyboardButton('specialization_2'))
keyboard_specialization.add(types.KeyboardButton('specialization_3'))


triple_answer = types.ReplyKeyboardMarkup(row_width=1)
triple_answer.add(types.KeyboardButton('Хорошие'))
triple_answer.add(types.KeyboardButton('Удовлетворительные'))
triple_answer.add(types.KeyboardButton('Неудовлетворительные'))


quad_answer = types.ReplyKeyboardMarkup(row_width=1)
quad_answer.add(types.KeyboardButton('Полностью обеспечены'))
quad_answer.add(types.KeyboardButton('Частично обеспечены'))
quad_answer.add(types.KeyboardButton('Слабо обеспечены'))
quad_answer.add(types.KeyboardButton('Не обеспечены'))

remove_keyboard = types.ReplyKeyboardRemove()
