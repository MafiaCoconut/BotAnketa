import telebot

import config.help_file as help_file
from config import settings
from config.help_file import *
from config.log_def import *
from handlers.authorization import get_fio, get_specialization
from handlers.admin import check_admin, get_questionnaires
from handlers.questionnaires import save_new_questionare, list_questionnaire, get_list_of_question
from models.keybords import *
import pandas as pd
from models.SQLite import get_person_data_from_id, delete_id_questioner

bot = telebot.TeleBot("5755365226:AAE9U5AtTrnUpPl5K1EIZxdOgLpl-4AFWDI")
tag = "main"
status = "debug"
authorization_command = '1'
count_questionnaire = 1
list_of_question = []
answers = []


@bot.message_handler(commands=['get_results', 'delete'])
def processing_admin_commands(message):
    function_name = "processing_admin_commands"
    set_func(function_name, tag, status)

    if check_admin(message):
        match message.text:
            case "/get_results":
                help_file.command_admin_panel = "get_results"
                set_inside_func("Вызвана функция получения результатов", function_name, tag)

            case "/delete":
                help_file.command_admin_panel = "delete"
                set_inside_func("Вызвана функция удаления анкеты", function_name, tag)

        main_processing_admin_panel(message)


@bot.message_handler(content_types=['document'])
def set_new_question(message):
    function_name = "set_new_question"
    set_func(function_name, tag, status)

    if check_admin(message):
        set_inside_func("Прислан документ", function_name, tag)
        save_new_questionare(message, bot)


@bot.message_handler(commands=['start'])
def start(message):
    function_name = "start"
    set_func(function_name, tag, status)
    set_person_text(function_name, tag, message)

    try:
        person = get_person_data_from_id(message.chat.id)
        bot.send_message(message.chat.id, f'Вы уже зарегестрировались {person[3]} {person[1]} {person[2]}', reply_markup=remove_keyboard)
    except:
        bot.send_message(message.chat.id, 'Добро пожаловать!', reply_markup=remove_keyboard)
        authorization(message)


@bot.message_handler(commands=['help'])
def help_function(message):
    function_name = "help_function"
    set_func(function_name, tag, status)
    set_person_text(function_name, tag, message)

    if check_admin(message):
        bot.send_message(message.chat.id, admin_commands)
        bot.send_message(message.chat.id, application_conditions)
        bot.send_message(message.chat.id, rules)
    else:
        bot.send_message(message.chat.id, rules)


def main_processing_admin_panel(message):
    function_name = "main_processing_results"
    set_func(function_name, tag, status)

    if message.text != "/exit":
        match help_file.command_admin_panel:
            case "get_results":
                if message.text == "/get_results":
                    get_questionnaires(message, bot)
                    bot.register_next_step_handler(message, main_processing_admin_panel)
                    set_inside_func("Отправлен список анкет", function_name, tag, status)

                else:
                    path = f"{path_to_answers}{message.text[0]}.xlsx"
                    with open(path, 'rb') as file:
                        bot.send_document(message.chat.id, file, reply_markup=remove_keyboard)
                    set_inside_func(f"Отправлен файл {path}", function_name, tag)

            case "delete":
                if message.text == "/delete":
                    get_questionnaires(message, bot)
                    bot.register_next_step_handler(message, main_processing_admin_panel)
                    set_inside_func("Отправлен список анкет", function_name, tag, status)

                elif help_file.delete_count == 0:
                    set_inside_func("Вызван повторный вопрос на удаление анкеты", function_name, tag, status)

                    bot.send_message(message.chat.id, f"Вы уверены, что хотите удалить анкету: {message.text}",
                                     reply_markup=keyboard_yes_no)
                    help_file.delete_count += 1
                    help_file.chose_questioner_to_delete = message.text
                    bot.register_next_step_handler(message, main_processing_admin_panel)

                elif help_file.delete_count == 1:
                    if message.text == "Да":
                        help_file.delete_count = 0

                        id_questioner = help_file.chose_questioner_to_delete[0]

                        path_answer = f"{path_to_answers}{id_questioner}.xlsx"
                        with open(path_answer, 'rb') as file:
                            bot.send_document(message.chat.id, file, reply_markup=remove_keyboard)
                        os.remove(path_answer)

                        path_question = f"{help_file.path_to_questions}/{id_questioner}"
                        os.remove(path_question)

                        delete_id_questioner(id_questioner)
                        set_inside_func(f"Удалена анкета: {help_file.chose_questioner_to_delete}", function_name, tag)

                    elif message.text == "Нет":
                        bot.send_message(message.chat.id, f"Выполнена отмена вызова функции "
                                                          f"{help_file.command_admin_panel}",
                                                          reply_markup=remove_keyboard)
                        help_file.delete_count = 0
                        set_inside_func("Отмена функции удаления анкеты", function_name, tag)

                    else:
                        bot.send_message(message.chat.id, "Вы ввели неправильный формат ответа, повторите попытку ещё "
                                                          "раз")
                        bot.register_next_step_handler(message, main_processing_admin_panel)
                        set_inside_func(f"Введён неправильный формат ответа: {message.text}",
                                        function_name, tag, "warning")

    else:
        bot.send_message(message.chat.id, f"Выполнена отмена вызова функции {help_file.command_admin_panel}",
                         reply_markup=remove_keyboard)
        set_inside_func("Отмена функции удаления анкеты", function_name, tag)


def work_with_questionnaire(message):
    function_name = "work_with_questionnaire"
    set_func(function_name, tag, status)
    try:
        if message.text[0] == "/":
            if message.text == "/exit":
                bot.send_message(message.chat.id, "Вы вернулись в главное меню", reply_markup=remove_keyboard)
            else:
                bot.send_message(message.chat.id, "Вы ввели команду, а не ответ, повторите попытку ещё раз")
                set_inside_func(f"Введён неправильный формат ответа: {message.text}", function_name, tag, "warning")

                bot.register_next_step_handler(message, work_with_questionnaire)

        else:
            global count_questionnaire, list_of_question, answers
            flag_end = False
            # flag_right_answer = True
            if count_questionnaire == 1:
                # TODO переделать определение id анкеты
                help_file.id_question_for_questioner = message.text.split()[0]
                list_of_question = get_list_of_question(help_file.id_question_for_questioner, message, bot)
                list_of_question.append("end")
                set_inside_func(f"|{message.from_user.username}| начал прохождение {message.text}",
                                function_name, tag)
                # print(list_of_question)
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
                save_answers(message)
    except:
        bot.send_message(message.chat.id, "Вы отправили не текст, Вы возвращены в главное меню",
                         reply_markup=remove_keyboard)
        # bot.register_next_step_handler(message, work_with_questionnaire)


def data_to_default():
    function_name = "data_to_default"
    set_func(function_name, tag, status)

    global answers, count_questionnaire, list_of_question
    answers = []
    count_questionnaire = 1
    list_of_question = []
    help_file.id_question_for_questioner = None

    set_inside_func("Переменные для прохождения анкеты были сброшены", function_name, tag, status)


def save_answers(message):
    function_name = "save_answers"
    set_func(function_name, tag, status)

    global answers

    data = get_person_data_from_id(message.chat.id)
    fio = f"{data[3]} {data[1]} {data[2]}"

    set_inside_func(f"|{message.from_user.username}| Ответы на анкету: {answers}", function_name, tag)

    path = f"{path_to_answers}{help_file.id_question_for_questioner}.xlsx"

    df = pd.read_excel(path)
    df[fio] = answers
    df.to_excel(path, index=False)

    data_to_default()


def one_question(message):
    function_name = "one_question"
    set_func(function_name, tag, status)

    text = list_of_question[count_questionnaire].split(' ')
    if text[0][4] == '1':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_1)
    elif text[0][4] == '2':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_2)
    elif text[0][4] == '3':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_3)
    elif text[0][4] == '4':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_4)
    elif text[0][4] == '5':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_5)
    elif text[0][4] == '6':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_6)
    elif text[0][4] == '7':
        bot.send_message(message.chat.id, ' '.join(text[1:]), reply_markup=answer_7)


def authorization(message):
    function_name = "authorization"
    set_func(function_name, tag, status)

    # print(message)
    try:
        if message.text in ["/begin", "/help"]:
            bot.send_message(message.chat.id, "Вы ввели команду, а не ответ, повторите попытку ещё раз")
            set_inside_func(f"Введён неправильный формат ответа: {message.text}", function_name, tag, "warning")
            bot.register_next_step_handler(message, authorization)
        else:
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
                        bot.send_message(message.chat.id, "Вы успешно зарегестрировались", reply_markup=remove_keyboard)
                        bot.send_message(message.chat.id, help_file.rules)
                    else:
                        bot.register_next_step_handler(message, authorization)
    except:
        bot.send_message(message.chat.id, "Вы отправили не текст, Вы возвращены в главное меню",
                         reply_markup=remove_keyboard)
        # bot.register_next_step_handler(message, work_with_questionnaire)

def authorization_command_plus_one():
    global authorization_command
    match authorization_command:
        case "1": authorization_command = "2"
        case "2": authorization_command = "original"


@bot.message_handler(commands=['begin'])
def main_menu(message):
    function_name = "main_menu"
    set_func(function_name, tag, status)

    person = get_person_data_from_id(message.chat.id)
    if person is not None:
        keyboard_questionnaires = list_questionnaire(message, bot)
        if message.text[1:] == "begin":
            bot.send_message(message.chat.id,
                             "Если хотите начать прохождение нажмите на кнопку с названием этой анкеты",
                             reply_markup=keyboard_questionnaires)
            bot.register_next_step_handler(message, work_with_questionnaire)
    else:
        bot.send_message(message.chat.id, "Вы ещё не зарегестрировались, для начала регистрации введите /start")
        set_inside_func(f"|{message.from_user.username}| начал проходить анкету не зарегестрировавшись",
                        function_name, tag)


if __name__ == '__main__':
    settings.main()
    # bot.polling(none_stop=True, timeout=3000000)
    bot.polling(none_stop=True)

# TODO: спец меню для админа
# TODO: проверка что файл подходит всем условиям
# TODO: добавить команду в админ панель, чтобы отправлять всем сообщение о новой анкете для прохождения

