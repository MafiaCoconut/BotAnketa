from telebot import types
import os


def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    return markup


path_to_questions = "data/Questionnaires/"
path_to_answers = "data/answers/"

# списка id админов
list_admins = ['603789543', '991027824']

# счётчик команд для регистрации
authorization_command = "1"

# тут хранится команда для админ панели
command_admin_panel = ""  # команда

# счётчик действий для удаления анкеты
delete_count = 0

# выбранная анкета для удаления
chose_questioner_to_delete = ""

# счётчик вопроса для прохождения анкеты
id_question_for_questioner = None

admin_commands = """Список команд доступных только админу:
/get_results -  Получить результаты определённой анкеты
/delete - Удалить анкету
/exit - Отмена вышеуказанных действий во время их выполнения
===========================
Чтобы добавить анкету, нужно отправить файл, который будет подходить под определённый условия
"""

application_conditions = """Анкета условия:
1. Первая строка - Название анкеты. Пример:
Название анкеты

2. Название раздела начинается с только одной цифры. Пример:
1 Название раздела

3. Вопрос записывается через 3 цифры и точки между ними, где первая цифра - номер раздела, вторая цифра - номер вопроса в разделе, третья цифра - вид ответов. Пример:
1.1.original Вопрос 1
1.2.4 Вопрос 2

Виды ответов в номерах:
3 -  Хорошие, Удовлетворительные, Неудовлетворительные
4 - Полностью обеспечены, Частично обеспечены, Слабо обеспечены, Не обеспечены"""

rules = """Правила использования данного бота:
- Чтобы начать проходить анкету наберите /begin
- Во время прохождения анкеты вы можете использовать кнопки для быстрого ввода ответа или в ручную отправь собственный ответ
- Данные сохраняются по окончанию прохождения анкеты
- Если вы хотите изменить ваш ответ, вы можете заного пройти анкету и старые ответы удалятся
- Чтобы вызвать это окно ещё раз, отправьте /help"""

list_of_specialization = ['монтажный отдел', 'сервисный отдел', 'проектный отдел']
