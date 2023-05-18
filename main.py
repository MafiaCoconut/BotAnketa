import telebot

from config import settings
from config.help_file import *
from config.log_def import *
from handlers.authorization import get_fio, get_specialization
from models.keybords import keyboard_specialization

# from selenium_group.selenium_main import get_data

bot = telebot.TeleBot("5755365226:AAE9U5AtTrnUpPl5K1EIZxdOgLpl-4AFWDI")
tag = "main"
status = "debug"
authorization_command = '1'


# TODO сделать отправку сообщения человеку чтобы он поменял свои данные а не создавал заново
@bot.message_handler(commands=['start'])
def start(message):
    function_name = "start"
    set_func(function_name, tag, status)

    bot.send_message(message.chat.id, 'Добро пожаловать!',
                     reply_markup=None)
    authorization(message)
    # bot.register_next_step_handler(message, authorization)


@bot.message_handler(commands=['main-menu'])
def main_menu(message):
    function_name = "main_menu"
    set_func(function_name, tag)





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

            else:
                bot.register_next_step_handler(message, authorization)


def authorization_command_plus_one():
    global authorization_command
    match authorization_command:
        case "1": authorization_command = "2"
        case "2": authorization_command = "3"


if __name__ == '__main__':
    settings.main()
    bot.polling(none_stop=True)
