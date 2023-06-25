from telebot import types
from config.help_file import list_of_specialization
keyboard_authorization = types.ReplyKeyboardMarkup(row_width=2)
keyboard_authorization.add(types.KeyboardButton('Да, я хочу сохранить'))
keyboard_authorization.add(types.KeyboardButton('Нет, я хочу изменить'))


keyboard_yes_no = types.ReplyKeyboardMarkup(row_width=2)
keyboard_yes_no.add(types.KeyboardButton('Да'))
keyboard_yes_no.add(types.KeyboardButton('Нет'))


keyboard_specialization = types.ReplyKeyboardMarkup(row_width=2)
for i in list_of_specialization:
    keyboard_specialization.add(types.KeyboardButton(i))
# keyboard_specialization.add(types.KeyboardButton('specialization_1'))
# keyboard_specialization.add(types.KeyboardButton('specialization_2'))
# keyboard_specialization.add(types.KeyboardButton('specialization_3'))


answer_1 = types.ReplyKeyboardMarkup(row_width=1)
answer_1.add(types.KeyboardButton('Хорошие'))
answer_1.add(types.KeyboardButton('Удовлетворительные'))
answer_1.add(types.KeyboardButton('Неудовлетворительные'))

answer_2 = types.ReplyKeyboardMarkup(row_width=1)
answer_2.add(types.KeyboardButton('Полностью обеспечены'))
answer_2.add(types.KeyboardButton('Частично обеспечены'))
answer_2.add(types.KeyboardButton('Слабо обеспечены'))
answer_2.add(types.KeyboardButton('Не обеспечены'))

answer_3 = types.ReplyKeyboardMarkup(row_width=1)
answer_3.add(types.KeyboardButton('Конфликты отсутствовали'))
answer_3.add(types.KeyboardButton('Имелись единичные не значительные конфликтные ситуации не влияющие на общий эмоциональный фон в бригаде'))
answer_3.add(types.KeyboardButton('Имелись серьезные конфликтные ситуации, негативно влияющие на общий эмоциональный фон в бригаде '))

answer_4 = types.ReplyKeyboardMarkup(row_width=1)
answer_4.add(types.KeyboardButton('Вопросы по начислению заработной платы отсутствуют'))
answer_4.add(types.KeyboardButton('Есть вопросы по начислению заработной платы '))


answer_5 = types.ReplyKeyboardMarkup(row_width=1)
answer_5.add(types.KeyboardButton('Был готов к выполнению работ'))
answer_5.add(types.KeyboardButton('В процессе работ выявилась необходимость изучения нового оборудования, требований по монтажу или технологий производства работ  '))

answer_6 = types.ReplyKeyboardMarkup(row_width=1)
answer_6.add(types.KeyboardButton('Ошибки отсутствовали'))
answer_6.add(types.KeyboardButton('Присутствовали незначительные ошибки'))
answer_6.add(types.KeyboardButton('Присутствовали значительные ошибки  '))

answer_7 = types.ReplyKeyboardMarkup(row_width=1)
answer_7.add(types.KeyboardButton('Простои отсутствовали'))
answer_7.add(types.KeyboardButton('Были не значительные простои'))
answer_7.add(types.KeyboardButton('Были значительные простои'))


remove_keyboard = types.ReplyKeyboardRemove()
