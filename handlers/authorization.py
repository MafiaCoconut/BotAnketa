import telebot

# from main import authorization
from config import settings
from config.help_file import *
from config.log_def import *
from models.SQLite import PersonSQLite
# from main import bot, authorization_command_plus_one
from models.data_classes import Persons
from models.keybords import keyboard_authorization, keyboard_specialization

tag = "authorization"
status = "debug"
flags = {
    "fio": 1,
    "specialization": 1,
}
data = {
    "first_name": str,
    "middle_name": str,
    "last_name": str,
    "specialization": None
}


def get_fio(message, bot):
    function_name = "get_fio"
    set_func(function_name, tag, status)

    global flags, data
    match flags["fio"]:
        case 1:
            set_inside_func(flags["fio"], function_name, tag, status)

            bot.send_message(message.chat.id, "Введите ваше ФИО через пробел", reply_markup=None)
            flags["fio"] += 1

        case 2:
            set_inside_func(flags["fio"], function_name, tag, status)

            text = message.text.split()
            if len(text) != 3:
                bot.send_message(message.chat.id, "Вы ввели неправильные данные, попробуйте ещё раз")
            else:
                set_inside_func(f"ФИО: {text}", function_name, tag)

                data['first_name'] = text[1]
                data['middle_name'] = text[2]
                data['last_name'] = text[0]

                if len(text) == 3:
                    bot.send_message(message.chat.id, f"Вы уверены что хотите сохранить: {' '.join(text)}",
                                     reply_markup=keyboard_authorization)

                flags["fio"] += 1

        case 3:
            set_inside_func(flags["fio"], function_name, tag, status)

            text = message.text
            if text not in ["Да, я хочу сохранить", "Нет, я хочу изменить"]:
                bot.send_message(message.chat.id, "Вы ввели неправильную команду, повторите попытку ещё раз")
                # bot.register_next_step_handler(message, authorization)
            else:
                match text:
                    case "Да, я хочу сохранить":
                        return True
                    case "Нет, я хочу изменить":
                        bot.send_message(message.chat.id, "Введите ваше ФИО через пробел", reply_markup=None)
                        flags["fio"] = 2
    return None


def get_specialization(message, bot):
    function_name = "get_specialization"
    set_func(function_name, tag, status)

    global flags
    match flags["specialization"]:
        case 1:
            set_inside_func(flags["specialization"], function_name, tag, status)

            bot.send_message(message.chat.id, "Выберите ваше название отдела",
                             reply_markup=keyboard_specialization)

            flags["specialization"] += 1

        case 2:
            set_inside_func(flags["specialization"], function_name, tag, status)

            text = message.text
            set_inside_func(f"Отдел: {text}", function_name, tag, status)
            data["specialization"] = text

            bot.send_message(message.chat.id, f"Вы уверены что хотите сохранить: {text}",
                             reply_markup=keyboard_authorization)

            flags["specialization"] += 1

        case 3:
            set_inside_func(flags["specialization"], function_name, tag, status)

            text = message.text
            if text not in ["Да, я хочу сохранить", "Нет, я хочу изменить"]:
                bot.send_message(message.chat.id, "Вы ввели неправильную команду, повторите попытку ещё раз")
                # bot.register_next_step_handler(message, authorization)
            else:
                match text:
                    case "Да, я хочу сохранить":
                        save_data(message)
                        return True

                    case "Нет, я хочу изменить":
                        bot.send_message(message.chat.id, "Выберите ваше название отдела",
                                         reply_markup=keyboard_specialization)
                        flags["specialization"] = 2

    return None


def save_data(message):
    function_name = "save_data"
    set_func(function_name, tag, status)

    global data
    person = PersonSQLite()
    args = Persons(id=str(message.chat.id),
                   first_name=data["first_name"],
                   middle_name=data["middle_name"],
                   last_name=data["last_name"],
                   specialization=data["specialization"])

    # TODO убрать эту строчку на релизе
    # person.clear_bd(Persons)

    person.set_person(args)
