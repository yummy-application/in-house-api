import sqlite3
from database.util import cursor_dict_factory


def create_table(table_name, number_of_seats, table_region):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO tables(name, seats, region) VALUES (?, ?, ?)", (table_name, number_of_seats, table_region))
        db.commit()

def table_exists(table_name) -> bool:
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tables WHERE name = ?", (table_name,))
        result = cursor.fetchone()
        return result is not None

def get_all_tables() -> list:
    with sqlite3.connect("restaurant.db") as db:
        db.row_factory  = cursor_dict_factory
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tables")
        return cursor.fetchall()

def deleteTable(table_name):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM tables WHERE name = ?", (table_name,))
        db.commit()

def update_table_status(table_name, new_status):
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE tables SET status = ? WHERE name = ?", (new_status, table_name))
        db.commit()