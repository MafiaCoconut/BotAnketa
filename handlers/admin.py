from config.help_file import list_admins


def check_admin(message):
    if str(message.chat.id) in list_admins:
        return True
    return False
