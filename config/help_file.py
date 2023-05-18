from telebot import types
import os


def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    return markup


link_menu = "https://studentenwerk-marburg.de/essen-trinken/speisekarte/"
link_authorization = "https://home.students.uni-marburg.de/login.php"

text_main_menu = """Выберите день для получения меню по нему:
1) Понедельник
2) Вторник
3) Среда
4) Четверг
5) Пятница
"""
#TODO: дополнять код при добавлении новых функций в групповой чат
text_help_group_menu = """Ниже предоставлены актуальные команды:
/mensa_n - Выводит меню в столовой за день n, где n - день недели
/pat - Требуется ответить на сообщение пользователя, котого хотите погладить 
/give_skotch - Требуется ответить на сообщение пользователя, которому хотите дать скотч
"""


def get_refactor_result_essen_menu(results, day):
    refactor_result = f"""Меню в Mensa на {day}\n{'-'*45}\n{results}"""
    return refactor_result
