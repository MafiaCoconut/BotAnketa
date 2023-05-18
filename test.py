# from openpyxl import Workbook, load_workbook
#
# import xlrd
# def all_none():
#     wb = Workbook()
#     sheet = wb.active
#
#     for i in range(1, 11):
#         for j in range(ord('A'), ord('O')):
#             x = f"{chr(j)}{i}"
#             sheet[x] = " "
#
#     wb.save('data/answers.xlsx')
#
# def clear():
#     wb = Workbook()
#     wb.save('data/answers.xlsx')
#
#
# def main():
#     answers = ['Хорошие', 'Слабо обеспечены', 'Полностью обеспечены']
#
#     # wb = Workbook()
#     # file = xlrd.open_workbook('data/answers.xlsx')
#     wb = load_workbook('data/answers.xlsx')
#     sheet = wb.active
#     #
#     sheet.cell(column=1, row=1, value="Вопросы\\ФИО")
#
#     # new_sheet = wb.create_sheet("Новый лист")
#     # wb.remove("Новый лист")
#
#     wb.save('data/answers.xlsx')

    # sheet.cell(column=1, row=2, value="Вопрос")
    # sheet.cell(column=1, row=3, value="Вопрос")
    # sheet.cell(column=1, row=4, value="Вопрос")
    # sheet.cell(column=2, row=1, value="FIO")
    # sheet.cell(column=3, row=1, value="FIO")
    # sheet.cell(column=4, row=1, value="FIO")
    # sheet.cell(column=5, row=1, value="FIO")


    # sheet["A1"].value = "Вопросы\\ФИО"
    # sheet["A2"].value = "Вопрос"
    # sheet["A3"].value = "Вопрос"
    # sheet["A4"].value = "Вопрос"
    # sheet["A5"].value = "Вопрос"
    #
    # sheet["B1"].value = "ФИО"
    # sheet["C1"].value = "ФИО"
    # sheet["D1"].value = "ФИО"
    # sheet["E1"].value = "ФИО"

    # wb = Workbook()
    # wb.save('balances.xlsx')







import pandas as pd
from config.help_file import *
from SQLite import get_person_data_from_id

path = "data/answers.xlsx"


def create_db():


    # Создание нового DataFrame
    # data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    data = {'Вопросы': []}
    df = pd.DataFrame(data)

    # Запись данных в файл XLSX
    df.to_excel(path, index=False)

    printi()


def main():
    answers = ['Хорошие', 'Слабо обеспечены', 'Полностью обеспечены']

    data = get_person_data_from_id("603789543")
    fio = f"{data[3]} {data[1]} {data[2]}"

    df = pd.read_excel(path)

    df[fio] = answers
    # Сохранение изменений в файл XLSX
    df.to_excel(path, index=False)

    printi()


def printi():
    df = pd.read_excel(path)
    print(df)


def new_list():
    writer = pd.ExcelWriter(path_to_questions, engine='xlsxwriter')

    # Создание нового листа
    df1 = pd.DataFrame({'Вопросы': []})
    df1.to_excel(writer, sheet_name='Заголовок 1')

    writer.save()
    print(writer)
if __name__ == '__main__':
    new_list()
    # main()
    # printi()
    # create_db()
    # clear()
    # all_none()

