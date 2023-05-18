from telebot import types
import os


def create_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    return markup


path_to_questions = "data/Questionnaires/"