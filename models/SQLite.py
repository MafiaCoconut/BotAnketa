import logging
import sqlite3
from models.data_classes import Persons
from dataclasses import asdict, astuple, dataclass
from config import settings
from config.log_def import *

tag = "SQLITE"


class SQLite:
    def __init__(self):
        self.connection = sqlite3.connect('data/db.sqlite')
        self.cursor = self.connection.cursor()

    def save_thing(self, *args):
        pass

    def create_bd(self, model):
        function_name = "create_bd"
        set_func(function_name, tag)

        self.cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {model.table} (
        id uuid PRIMARY KEY,
        first_name TEXT,
        middle_name TEXT,
        last_name TEXT,
        specialization TEXT,
        created timestamp with time zone
        );""")
        logging.info("Успешно")
        self.connection.commit()

    def clear_bd(self, model):
        function_name = "clear_bd"
        set_func(function_name, tag)

        self.cursor.execute(f"""DELETE FROM {model.table};""")
        self.connection.commit()

    def delete_bd(self, model):
        function_name = "delete_bd"
        set_func(function_name, tag)

        self.cursor.execute(f"""DROP table {model.table};""")
        self.connection.commit()

    def get_bd(self, model):
        function_name = "get_bd"
        set_func(function_name, tag)

        self.cursor.execute(f"""SELECT * FROM {model.table};""")
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def turn_off(self):
        function_name = "turn_off"
        set_func(function_name, tag)

        self.cursor.close()
        self.connection.close()


class PersonSQLite(SQLite):
    def __init__(self):
        super().__init__()
        self.table = "persons"

    def set_person(self, model):
        function_name = "set_person"
        set_func(function_name, tag)

        args = [model.id, model.first_name, model.middle_name, model.last_name, model.specialization, model.created, ]
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE id = ?", (model.id, ))
            result = self.cursor.fetchone()
            if result[0] == 0:
                sqlite_insert_query = f"""
                INSERT INTO {self.table}
                (id, first_name, middle_name, last_name, specialization, created)
                VALUES (?, ?, ?, ?, ?, ?);
               """

                self.cursor.execute(sqlite_insert_query, args)
                self.connection.commit()
            else:
                set_inside_func("Человек уже есть в БД", function_name, tag)
        except:
            set_inside_func("Человек уже есть в БД", function_name, tag)


# def send_data_essen(self, data):
#      function_name = "send_data_essen"
#      set_func(function_name, tag)
#
#      args = [str(data.id), data.title, data.type, data.price, data.tag, data.created, ]
#      try:
#          self.cursor.execute(f"SELECT COUNT(*) FROM {self.table} WHERE title = ?", (data.title, ))
#
#          result = self.cursor.fetchone()
#          if result[0] == 0:
#              sqlite_insert_query = f"""-- INSERT INTO {self.table}
#                                   (id, title, type, price, tag, created)
#                                   VALUES (?, ?, ?, ?, ?, ?);"""
# logging.info(f"Добавлено в бд: {args}")
#              self.cursor.execute(sqlite_insert_query, args)
#              self.connection.commit()
#          else:
#              set_inside_func(f"Запись уже есть в бд: {args}", function_name, tag)
#              logging.info(f"Запись уже есть в бд: {args}")
# except sqlite3.IntegrityError:
#     set_inside_func(f"Запись уже есть в бд: {args}", function_name, tag)
#

def set_data_person(fio):
    person = PersonSQLite
    person.set_person(fio)
    person.turn_off()


def main():
    sql = SQLite()
    sql.create_bd(Persons)
    # sql.delete_bd(Persons)
    sql.turn_off()


if __name__ == '__main__':
    settings.main()
    main()
    # with sqlite3.connect('data/menu.sqlite') as sqlite_conn:
    #     main(sqlite_conn)
