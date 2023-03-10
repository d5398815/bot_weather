import sqlite3
import os.path
import json


def exists_file():
    filename = "mydatabase.db"

    if os.path.isfile(filename):
        return True
    else:
        return False


def read_id():
    if not exists_file():
        return False
    else:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        
        return rows

#print(read_id())


def creating_file(chat_id, message_text):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""CREATE TABLE users (chat_id text, status text)""")
    data = [(chat_id, message_text)]

    cursor.executemany("INSERT INTO users VALUES (?,?)", data)

    # Сохраняем изменения
    conn.commit()


def del_user(chat_id):
    # Сука нах, вечер на это убил, не менять потому что иначе None == False
    if check_subscribe(chat_id) == False:
        return "Подписка отсутствует"

    else:

        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        sql = "DELETE FROM users WHERE chat_id=?"
        cursor.execute(sql, [chat_id])

        conn.commit()

        return "Подписка удалена!"


# Возвращает False если нет в базе
def check_subscribe(chat_id):
    if not exists_file():
        return False

    else:

        # cursor = search_id(chat_id)[0]
        # conn = search_id(chat_id)[-1]
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        sql = "SELECT * FROM users WHERE chat_id=?"
        search_chat_id = cursor.execute(sql, [chat_id])



        # Если в базе нет такой записи выбивает исключение и фозвращает False
        try:
            cursor.fetchone()[-1] == "Подписка на погоду"
        except TypeError as e:
            return "Подписка активирована!"

        # return "Вы уже подписаны"
        conn.commit()


"""
    try:
        sql = "SELECT * FROM users WHERE chat_id=?"
        cursor.execute(sql, [chat_id])
    except:
        return "Подписка активирована!"

    return True """


def write_file(chat_id, message_text="Подписка на погоду"):
    if not exists_file():

        creating_file(chat_id, message_text)

        return "Подписка активирована!"

    else:

        # Если юзера нет в базе записываем
        if check_subscribe(chat_id) == "Подписка активирована!":

            conn = sqlite3.connect("mydatabase.db")
            cursor = conn.cursor()

            data = [(chat_id, message_text)]

            cursor.executemany("INSERT INTO users VALUES (?,?)", data)

            # Сохраняем изменения
            conn.commit()

            return "Подписка активирована!"

        # Если юзер есть
        else:
            return "Вы уже подписаны"
            # cursor.fetchone()[-1] == "Подписка на погоду":


def subscribe(chat_id, message_text):
    if message_text == "Подписка на погоду":
        return write_file(chat_id)

    elif message_text == "Отписаться":
        return del_user(chat_id)


# print(subscribe("rr", "Подписка на погоду"))
# print(check_subscribe("rr"))
# print(exists_file())
