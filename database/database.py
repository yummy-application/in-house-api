import sqlite3

def default_db_setup():
    with sqlite3.connect("restaurant.db") as db:
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS restaurant(name Text, image Text)")
        cursor.execute("CREATE TABLE IF NOT EXISTS validation(pw_hash Text)")
        db.commit()
