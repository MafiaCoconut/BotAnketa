import logging
import sqlite3
from models.data_classes import Persons, Questionnaires
from dataclasses import asdict, astuple, dataclass
from config import settings
from config.log_def import *

tag = "SQLITE_all"
status = "debug"

class SQLite:
    def __init__(self):
        self.connection = sqlite3.connect("data/db.sqlite")
        # self.connection = sqlite3.connect("../data/db.sqlite")
        self.cursor = self.connection.cursor()
        self.tag = "SQLITE"

    def save_thing(self, *args):
        pass

    def clear_bd(self, model):
        function_name = "clear_bd"
        set_func(function_name, self.tag)

        self.cursor.execute(f"""DELETE FROM {model.table};""")
        self.connection.commit()

    def delete_bd(self, model):
        function_name = "delete_bd"
        set_func(function_name, self.tag)

        self.cursor.execute(f"""DROP table {model.table};""")
        self.connection.commit()

    def get_bd(self, model):
        function_name = "get_bd"
        set_func(function_name, self.tag)

        self.cursor.execute(f"""SELECT * FROM {model.table};""")
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def turn_off(self):
        function_name = "turn_off"
        set_func(function_name, self.tag)

        self.cursor.close()
        self.connection.close()


class PersonSQLite(SQLite):
    def __init__(self):
        super().__init__()
        self.tag = "PersonSQLite"

    def create_bd(self):
        function_name = "create_bd"
        set_func(function_name, self.tag)

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS persons (
        id uuid PRIMARY KEY,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        specialization TEXT,
        created timestamp with time zone
        );""")
        set_inside_func(f"DB: persons была успешно добавлена", function_name, self.tag)
        self.connection.commit()

    def set_person(self, model):
        function_name = "set_person"
        set_func(function_name, self.tag)

        args = [str(model.id), model.first_name, model.middle_name, model.last_name, model.specialization, model.created]

        for i in args:
            print(f"{i}, {type(i)}")
        sqlite_insert_query = f"""
        INSERT INTO {model.table}
        (id, first_name, middle_name, last_name, specialization, created)
        VALUES (?, ?, ?, ?, ?, ?);
       """

        self.cursor.execute(sqlite_insert_query, args)
        self.connection.commit()

    def get_data_from_id(self, need_id):
        function_name = "get_id"
        set_func(function_name, self.tag)

        self.cursor.execute(f"SELECT * FROM persons WHERE id={need_id}")
        data = self.cursor.fetchone()
        return data


class QuestionnairesSQLite(SQLite):
    def __init__(self):
        super().__init__()
        self.tag = "QuestionnairesSQLite"

    def create_bd(self):
        function_name = "create_bd"
        set_func(function_name, self.tag)

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS questionnaires (
        id uuid PRIMARY KEY,
        title TEXT,
        link TEXT,
        created timestamp with time zone
        );""")
        set_inside_func(f"DB: questionnaires была успешно добавлена", function_name, self.tag)
        self.connection.commit()

    def get_last_id(self):
        function_name = "get_last_id"
        set_func(function_name, self.tag)

        self.cursor.execute(f"SELECT COUNT(*) FROM questionnaires")
        return self.cursor.fetchone()[0]

    def set_data(self, model):
        function_name = "set_person"
        set_func(function_name, self.tag)

        args = [model.id, model.title, model.link, model.created]

        sqlite_insert_query = f"""
                        INSERT INTO {model.table}
                        (id, title, link, created)
                        VALUES (?, ?, ?, ?);
                       """

        self.cursor.execute(sqlite_insert_query, args)
        self.connection.commit()

    def get_need_question(self, need_id):
        function_name = "get_need_question"
        set_func(function_name, self.tag)

        self.cursor.execute(f"SELECT * FROM questionnaires WHERE id={need_id}")
        data = self.cursor.fetchone()
        return data

    def delete_questioner(self, id_questioner):
        function_name = "delete_questioner"
        set_func(function_name, tag)

        condition = f"id = {id_questioner}"
        query = f"DELETE FROM questionnaires WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()


def get_person_data_from_id(need_id):
    function_name = "get_id"
    set_func(function_name, tag, status)
    Person = PersonSQLite()
    data = Person.get_data_from_id(need_id)
    Person.turn_off()
    return data


def delete_id_questioner(id_questioner):
    function_name = "delete_id_questioner"
    set_func(function_name, tag, status)

    Questioner = QuestionnairesSQLite()
    Questioner.delete_questioner(id_questioner)
    set_inside_func("Удаление произошло успешно", function_name, tag)
    Questioner.turn_off()


def main():
    sql = PersonSQLite()

    # sql.delete_bd(Questionnaires)
    sql.create_bd()

    sql.turn_off()


def ques():
    # question = QuestionnairesSQLite("../data/db.sqlite")
    question = QuestionnairesSQLite()

    # question.delete_bd(Questionnaires)
    question.create_bd()

    question.turn_off()


if __name__ == '__main__':
    settings.main()
    main()
    # ques()
    # with sqlite3.connect('data/menu.sqlite') as sqlite_conn:
    #     main(sqlite_conn)
