import sqlite3

from database.setup import default_db_setup


def restaurant_already_exists() -> bool:
    default_db_setup()
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM restaurant")
        return cursor.fetchone() is not None

def create_restaurant(name, image):
    default_db_setup()
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO restaurant VALUES (?, ?)", (name, image))
        db.commit()

def full_restaurant_info() -> dict:
    default_db_setup()
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM restaurant")
        return cursor.fetchone()