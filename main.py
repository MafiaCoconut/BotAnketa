import telebot

from config import settings
from config.help_file import *
from config.log_def import *
from handlers.authorization import get_fio, get_specialization
from handlers.questionnaires import save_new_questionare, list_questionnaire, get_list_of_question
from models.keybords import *
import pandas as pd
from models.SQLite import get_person_data_from_id

# from selenium_group.selenium_main import get_data

bot = telebot.TeleBot("5755365226:AAE9U5AtTrnUpPl5K1EIZxdOgLpl-4AFWDI")
tag = "main"
status = "debug"
authorization_command = '0'
admin_ids = ['603789543', ]
count_questionnaire = 1
list_of_question = []
id_question = None
answers = []


def admin_only(func):
    def wrapper(message):
        if message.from_user.id in admin_ids:
            func(message)
        else:
            bot.reply_to(message, "У вас нет прав доступа.")
    return wrapper


# TODO сделать отправку сообщения человеку чтобы он поменял свои данные а не создавал заново
@bot.message_handler(commands=['start'])
def start(message):
    function_name = "start"
    set_func(function_name, tag, status)

    bot.send_message(message.chat.id, 'Добро пожаловать!',
                     reply_markup=None)
    authorization(message)
    # bot.register_next_step_handler(message, authorization)


@bot.message_handler(commands=['list', 'begin'])
def main_menu(message):
    function_name = "main_menu"
    set_func(function_name, tag, status)

    keyboard_questionnaires = list_questionnaire(message, bot)
    if message.text[1:] == "begin":
        bot.send_message(message.chat.id,
                         "Если хотите начать прохождение нажмите на кнопки с названием этой анкеты",
                         reply_markup=keyboard_questionnaires)
        bot.register_next_step_handler(message, work_with_questionnaire)


def work_with_questionnaire(message):
    function_name = "work_with_questionnaire"
    set_func(function_name, tag, status)

    global count_questionnaire, list_of_question, answers, id_question
    flag_end = False
    # need_id = message.text[0]
    if count_questionnaire == 1:
        id_question = message.text[0]
        list_of_question = get_list_of_question(id_question, message, bot)
    else:
        answers.append(message.text)

    text = list_of_question[count_questionnaire].split(' ')
    if len(text[0]) == 1:
        bot.send_message(message.chat.id, f"{text[0]}) {' '.join(text[1:])}", reply_markup=remove_keyboard)
        count_questionnaire += 1
        text = list_of_question[count_questionnaire].split(' ')

    if len(text[0]) == 5:
        one_question(message)

    elif text[0] == "end":
        flag_end = True

    if not flag_end:
        count_questionnaire += 1
        bot.register_next_step_handler(message, work_with_questionnaire)
    else:
        bot.send_message(message.chat.id, "Ваши данные сохранены", reply_markup=remove_keyboard)
        set_inside_func(answers, function_name, tag)
        save_answers(message)


def data_to_default():
    global answers, count_questionnaire, list_of_question, id_question
    answers = []
    count_questionnaire = 1
    list_of_question = []
    id_question = None


@bot.message_handler(commands=['test'])
def save_answers(message):
    function_name = "save_answers"
    set_func(function_name, tag, status)

    global answers

    data = get_person_data_from_id(message.chat.id)
    fio = f"{data[3]} {data[1]} {data[2]}"

    path = f"{path_to_answers}{id_question}.xlsx"

    df = pd.read_excel(path)
    df[fio] = answers
    df.to_excel(path, index=False)

    data_to_default()


def one_question(message):
    function_name = "one_question"
    set_func(function_name, tag, status)

    text = list_of_question[count_questionnaire].split(' ')
    # set_inside_func(' '.join(text), function_name, tag)
    if text[0][4] == '3':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=triple_answer)
    elif text[0][4] == '4':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=quad_answer)


@admin_only
@bot.message_handler(content_types=['document'])
def set_new_question(message):
    function_name = "set_new_question"
    set_func(function_name, tag, status)

    save_new_questionare(message, bot)


def authorization(message):
    function_name = "authorization"
    set_func(function_name, tag, status)

    match authorization_command:
        case "1":
            if get_fio(message, bot):
                authorization_command_plus_one()
                authorization(message)
            else:
                bot.register_next_step_handler(message, authorization)

        case "2":
            if get_specialization(message, bot):
                authorization_command_plus_one()
                bot.send_message(message.chat.id, "Вы успешно зарегестрировались", reply_markup=None)
            else:
                bot.register_next_step_handler(message, authorization)


def authorization_command_plus_one():
    global authorization_command
    match authorization_command:
        case "1": authorization_command = "2"
        case "2": authorization_command = "3"


if __name__ == '__main__':
    settings.main()
    bot.polling(none_stop=True, timeout=3000000)
