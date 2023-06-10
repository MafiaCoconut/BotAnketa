from telebot import types
import os


def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    return markup


path_to_questions = "data/Questionnaires/"
path_to_answers = "data/answers/"
# count_questionnaire = 1

admin_commands = """Список команд доступных только админу:
/get_results -  Получить результаты определённой анкеты
"""