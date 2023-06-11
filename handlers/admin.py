from config.help_file import list_admins
from handlers.questionnaires import list_questionnaire


def check_admin(message):
    if str(message.chat.id) in list_admins:
        return True
    return False


def get_questionnaires(message, bot):
    keyboard_questionnaires = list_questionnaire(message, bot)
    bot.send_message(message.chat.id, "Выберите анкету с которой хотите выполнить это действие, для этого нажмите "
                                      "необходимую кнопку", reply_markup=keyboard_questionnaires)
