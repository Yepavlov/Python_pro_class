import os
import sqlite3

current_directory = os.path.dirname(__file__)
database_path = os.path.join(current_directory, '../blueprints/chinook.db')


def execute_query(query: str, args=()):
    with sqlite3.connect(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        result = cursor.fetchall()
    return result
