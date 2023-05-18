import telebot

from config import settings
from config.help_file import *
from config.log_def import *
from models.SQLite import PersonSQLite, QuestionnairesSQLite
# from main import bot, authorization_command_plus_one
from models.data_classes import Persons, Questionnaires
from models.keybords import *

tag = "questionare"
status = "debug"


def save_data(message, bot, link):
    file_info = bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    downloaded_file = bot.download_file(file_path)

    with open(link, 'wb') as file:
        file.write(downloaded_file)


def save_new_questionare(message, bot):
    function_name = "set_new_question"
    set_func(function_name, tag, status)

    questioner = QuestionnairesSQLite()
    need_id = int(questioner.get_last_id()) + 1
    link = f"{path_to_questions}{need_id}"

    save_data(message, bot, link)

    with open(link, 'r') as file:
        content = file.read()

    context = content.split("\n")
    title = context[0]
    need_id = str(need_id)
    model = Questionnaires(id=need_id, title=title, link=link)
    questioner.set_data(model)

    bot.reply_to(message.chat.id, f'Содержимое файла:\n{content}', reply_markup=None)
    set_inside_func(f"Файл: {title} успешно сохранён", function_name, tag)


def list_questionnaire(message, bot):
    function_name = "set_new_question"
    set_func(function_name, tag, status)
    # set_func(function_name, tag)

    questioner = QuestionnairesSQLite()
    data = questioner.get_bd(Questionnaires)
    result = "Доступные анкеты\n"
    keyboard_questionnaires = types.ReplyKeyboardMarkup(row_width=2)

    for block in data:
        result += f"{block[0]}) {block[1]}\n"
        keyboard_questionnaires.add(f"{block[0]}-{block[1]}")
    bot.send_message(message.chat.id, f'{result}', reply_markup=remove_keyboard)
    return keyboard_questionnaires


def get_list_of_question(need_id, message, bot):
    function_name = "get_list_of_question"
    set_func(function_name, tag, status)

    questioner = QuestionnairesSQLite()
    data = questioner.get_need_question(need_id)
    set_inside_func(data, function_name, tag)

    path = data[2]

    with open(path, 'r') as file:
        result = file.read()

    list_of_question = result.split("\n")

    return list_of_question


if __name__ == '__main__':
    pass
    # get_one_question(2)

    # quest = QuestionnairesSQLite()
    # last_id = quest.get_last_id()
    # print(last_id)



